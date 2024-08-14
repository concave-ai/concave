from pydantic import BaseModel


class SpaceConfig(BaseModel):
    name: str
    language: str
    version: str
    codebase: str
