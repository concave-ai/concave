from pydantic import BaseModel


class SpaceConfig(BaseModel):
    language: str
    version: str
    codebase: str
