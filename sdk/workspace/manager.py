from typing import List

from sdk.workspace.workspace import Workspace


class WorkspaceManager:

    def create(self, config: dict) -> Workspace:
        pass

    def list(self) -> List[Workspace]:
        pass

    def get(self, workspace: str) -> Workspace:
        pass

    def rm(self, workspace: Workspace | str):
        pass
