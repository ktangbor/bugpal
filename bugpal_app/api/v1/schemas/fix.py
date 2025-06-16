from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class FixBase(BaseModel):
    description: str = Field(..., max_length=3000)

class FixCreate(FixBase):
    pass

class FixInDB(FixBase):
    id: int
    issue_id: int
    user_id: int|None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class FixPublic(FixInDB):
    vote_score: Optional[int] = 0
