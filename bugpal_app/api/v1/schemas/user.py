from pydantic import BaseModel, Field, ConfigDict

class UserBase(BaseModel):
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=50)

class UserCreate(UserBase):
    pass


class UserInDB(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserPublic(UserInDB):
    pass
