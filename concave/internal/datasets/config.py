from concave.internal.datasets.swe_bench.constants import MAP_REPO_VERSION_TO_SPECS
from concave.internal.workspace.config import Config


def get_config_from_swe_bench(name: str, repo: str, version: str, base_commit: str):
    SPCE_MAPS = MAP_REPO_VERSION_TO_SPECS[repo]
    spec = SPCE_MAPS[version]
    setup = [spec["install"]]
    if "pip_packages" in spec:
        setup.append('pip install {}'.format(
            " ".join(spec["pip_packages"])
        ))

    return Config(
        name=name,
        language='python',
        version=f'{spec["python"]}-alpine3.13',
        codebase=f'github.com/pytest-dev/pytest/commit/{base_commit}',
        project_setup=setup
    )
