from pydantic import BaseModel


class Config(BaseModel):
    language: str
    version: str
    codebase: str
