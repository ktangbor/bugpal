from sqlalchemy.ext.asyncio import AsyncSession

from bugpal_app.repos.user import UserRepository
from bugpal_app.api.v1.schemas.user import UserCreate
from bugpal_app.models.user import User

class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    def create_user(self, user: UserCreate) -> User:
        return self.repo.create(user)

    def get_user(self, user_id: int) -> User|None:
        return self.repo.get(user_id)

    def list_users(self) -> list[User]:
        return self.repo.list()
