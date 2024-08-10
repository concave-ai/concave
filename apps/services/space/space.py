import os.path
import tempfile
import uuid

import docker
from docker.api import container
from loguru import logger

import jinja2

from apps.services.space.constants import Status, SpaceConfig


class Workspace:
    status: Status = Status.UNKNOWN

    def __init__(self, uuid):
        self.uuid = uuid

    @classmethod
    def create(cls, config=SpaceConfig):
        return Workspace('uuid')



def parse_codebase(codebase: str):
    parts = codebase.split('/')
    if len(parts) == 3:
        return codebase, None
    elif len(parts) == 5:
        return '/'.join(parts[:3]), parts[-1]

    raise ValueError("Invalid codebase: %s, excepted github.com/{repo}/{org}?(/commit/{commit})" % codebase)


class WorkspaceCreator:

    def __init__(self, config=SpaceConfig, debug=False):
        self.config = config
        self.uuid = str(uuid.uuid4())
        self.temp_dir = tempfile.mkdtemp("concave")
        self.repo, self.commit = parse_codebase(self.config.codebase)
        try:
            self.docker = docker.from_env()
        except Exception as e:
            logger.error(f"Failed to connect to Docker: {e}")
            raise e

    def create(self):
        self.prepare()
        return Workspace.create(self.config)

    def prepare(self):
        logger.debug(f"Workspace temp dir: {self.temp_dir}")
        assert self.config.language in ['python'], f"Unsupported language: {self.config.language}"

        dockerfile = jinja2.Template(
            open(f"{os.path.dirname(__file__)}/Dockerfile.j2").read()
        ).render(
            IMAGE_NAME=self.config.language,
            IMAGE_TAG=self.config.version,
            GIT_REPO=self.repo,
            GIT_COMMIT=self.commit,
        )

        with open(f"{self.temp_dir}/Dockerfile", "w") as f:
            f.write(dockerfile)

        logger.debug(f"Generated Dockerfile: ===\n{dockerfile}\n===")
        logger.debug("Building Docker image")

        images, logs = self.docker.images.build(
            path=self.temp_dir,
            tag=f"concave-space:{self.uuid}",
            labels={
                "concave.space.uuid": self.uuid,
                "concave.space.repo": self.repo,
                "concave.space.commit": self.commit,
            }
        )

        logger.debug(f"Docker image built: concave-space:{self.uuid}")


