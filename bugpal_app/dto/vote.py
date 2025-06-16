from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class VoteBase(BaseModel):
    value: int = Field(..., ge=-1, le=1)


class VoteCreate(VoteBase):
    pass


class VoteInDB(VoteBase):
    id: int
    user_id: int
    fix_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

