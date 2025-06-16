from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from bugpal_app.api.v1.schemas.user import UserCreate
from bugpal_app.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: UserCreate) -> User:
        user_db = User(**user.model_dump())
        self.session.add(user_db)
        await self.session.flush()
        return user_db

    async def get(self, user_id: int) -> User|None:
        result =  await self.session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalars().first()

    async def list(self) -> list[User]:
        result =  await self.session.execute(
            select(User).order_by(User.id.desc())
        )
        return result.scalars().all()
