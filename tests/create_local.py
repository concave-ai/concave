import sys

from concave.internal.workspace.config import Config
from concave.internal.workspace.manager import WorkspaceManager
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="DEBUG")


# https://github.com/pytest-dev/pytest/pull/7432
def main():
    config = Config(
        language='python',
        version='3.8-alpine3.13',
        codebase='github.com/pytest-dev/pytest/commit/4d439760adddc2161517188e16e2adf11ac4ac38',
        project_setup=[
            'python -m pip install --upgrade pip',
            'pip install --upgrade wheel setuptools tox',
            'python setup.py sdist bdist_wheel',
        ]
    )

    manager = WorkspaceManager()

    workspace = manager.create(config)
    logger.info(f'Workspace created: {workspace.id()}')

    logger.info(f'Workspace ls /workspace/app: {workspace.ls("/workspace/app")}')

    logger.info(f'list current workspaces: {[workspace.id() for workspace in manager.list()]}')

    f = workspace.open("/workspace/app/README.rst")
    logger.info(f'file original content: {f.read()}')

    f.write("""multi line
test\"abc
123""")
    logger.info(f'file modified content: {f.read()}')

    f.append("append content")
    logger.info(f'file appended content: {f.read()}')

    snapshot = workspace.commit()
    logger.info(f'commit snapshot: {snapshot}')

    logger.info(f'remove workspace: {workspace.id()}')
    workspace.remove()

    workspace1 = manager.run(snapshot)
    logger.info(f'run snapshot: {workspace1.id()}')

    f1 = workspace1.open('/workspace/app/README.rst')
    logger.info(f'read file: {f1.read()}')

    logger.info('remove workspace1')
    workspace1.remove()


if __name__ == '__main__':
    main()
