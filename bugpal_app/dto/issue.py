from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class IssueBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: str|None = None


class IssueCreate(IssueBase):
    pass


class IssueInDB(IssueBase):
    id: int
    user_id: int|None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class IssuePublic(IssueInDB):
    pass
