from enum import Enum
from pydantic import BaseModel, ValidationError


class Status(str, Enum):
    ACTIVE = 'active'
    PENDING = 'pending'
    DELETED = 'deleted'
    UNKNOWN = 'unknown'


class SpaceConfig(BaseModel):
    language: str
    version: str
    codebase: str
