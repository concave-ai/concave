import sys

from concave.internal.datasets.swe_bench.constants import SPECS_PYTEST
from concave.internal.workspace.config import Config
from concave.internal.workspace.manager import WorkspaceManager
from loguru import logger


def main():
    config = Config(
        name="pytest_10081",
        language='python',
        version='3.9-alpine3.13',
        codebase='github.com/pytest-dev/pytest/commit/e6e300e729dd33956e5448d8be9a0b1540b4e53a',
        project_setup=[
            'python -m pip install -e .',
            'pip install {}'.format(
                " ".join(SPECS_PYTEST["5.4"]["pip_packages"])
            )
        ]
    )

    manager = WorkspaceManager()

    workspace = manager.create(config)
    logger.info(f'Workspace created: {workspace.id()}')

    logger.info(f'Workspace ls /workspace/app: {workspace.ls("/workspace/app")}')

    logger.info(f'remove workspace: {workspace.id()}')
    workspace.remove()


if __name__ == '__main__':
    main()
