from dataclasses import dataclass
from pydantic import EmailStr


@dataclass
class UserBaseDTO:
    username: str
    email: EmailStr

class UserCreate(UserBaseDTO):
    pass


class UserInDB(UserBaseDTO):
    id: int


class UserPublic(UserInDB):
    pass
