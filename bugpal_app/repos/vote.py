from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from bugpal_app.models.vote import Vote
from bugpal_app.api.v1.schemas.vote import VoteCreate


class VoteRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, vote: VoteCreate) -> Vote:
        vote_db = Vote(**vote.model_dump())
        self.session.add(vote_db)
        await self.session.flush()

        return vote_db

    async def get(self, vote_id: int) -> Vote|None:
        result = await self.session.execute(
            select(Vote).where(Vote.id == vote_id)
        )

        return result.scalar_one()

    async def list_by_