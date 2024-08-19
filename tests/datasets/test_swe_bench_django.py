import sys

from concave.internal.datasets.swe_bench.constants import SPECS_PYTEST, SWEbenchInstance
from concave.internal.workspace.config import Config
from concave.internal.workspace.manager import WorkspaceManager
from loguru import logger

from internal.datasets.config import get_config_from_swe_bench


def main():
    config = get_config_from_swe_bench(
        instance=SWEbenchInstance(
            instance_id="django__django-13925",
            repo="django/django",
            version="4.0",
            base_commit="0c42cdf0d2422f4c080e93594d5d15381d6e955e",
            patch="",
            test_patch="",
            problem_statement="",
            hints_text="",
            created_at="",
            FAIL_TO_PASS="",
            PASS_TO_PASS="",
            environment_setup_commit="475cffd1d64c690cdad16ede4d5e81985738ceb4",
        )
    )
    for setup in config.env_script_list:
        print(setup)

    print(config.env_image_key)
    print(config.workspace_image_key)
    manager = WorkspaceManager()

    workspace = manager.create(config)
    logger.info(f'Workspace created: {workspace.id()}')

    logger.info(f'Workspace ls /workspace/app: {workspace.ls("/workspace/app")}')

    logger.info(f'remove workspace: {workspace.id()}')
    workspace.remove()


if __name__ == '__main__':
    main()
