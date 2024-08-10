import sys

from apps.services.space.constants import SpaceConfig
from apps.services.space.space import Workspace, WorkspaceCreator
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="DEBUG")


# https://github.com/pytest-dev/pytest/pull/7432
def main():
    config = SpaceConfig(
        language='python',
        version='3.8',
        codebase='github.com/pytest-dev/pytest/commit/678c1a0745f1cf175c442c719906a1f13e496910'
    )

    c = WorkspaceCreator(config)
    c.create()


if __name__ == '__main__':
    main()
