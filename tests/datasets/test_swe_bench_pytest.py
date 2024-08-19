import sys

from concave.internal.datasets.swe_bench.constants import SPECS_PYTEST, SWEbenchInstance
from concave.internal.workspace.config import Config
from concave.internal.workspace.manager import WorkspaceManager
from loguru import logger

from internal.datasets.config import get_config_from_swe_bench


def main():
    config = get_config_from_swe_bench(
        instance=SWEbenchInstance(
            instance_id="pytest-dev__pytest-6202",
            repo="pytest-dev/pytest",
            version="5.2",
            base_commit="3a668ea6ff24b0c8f00498c3144c63bac561d925",
            patch="",
            test_patch="",
            problem_statement="",
            hints_text="",
            created_at="",
            FAIL_TO_PASS="",
            PASS_TO_PASS="",
            environment_setup_commit="",
        )
    )
    for setup in config.env_script_list:
        print(setup)

    manager = WorkspaceManager()

    workspace = manager.create(config)
    logger.info(f'Workspace created: {workspace.id()}')

    logger.info(f'Workspace ls /workspace/app: {workspace.ls("/workspace/app")}')

    logger.info(f'remove workspace: {workspace.id()}')
    workspace.remove()


if __name__ == '__main__':
    main()
