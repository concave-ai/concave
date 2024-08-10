from sdk.workspace.file import File


class Workspace:
    status: str

    def commit(self) -> str:
        pass

    # def fork(self) -> 'Workspace':
    #     uid = self.commit()
    #     pass

    def execute(self, command: str, **kwargs) -> int:
        pass

    def quit(self):
        pass

    def ls(self, path: str) -> list[str]:
        pass

    def open(self) -> File:
        pass
