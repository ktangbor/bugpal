from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from bugpal_app.models.fix import Fix
from bugpal_app.api.v1.schemas.fix import FixCreate

class FixRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, fix: FixCreate, user_id: int) -> Fix:
        fix_db = Fix(**fix.model_dump(), user_id=user_id)
        self.session.add(fix_db)
        await self.session.flush()
        return fix_db

    async def get(self, fix_id: int) -> Fix|None:
        result =  await self.session.execute(
            select(Fix).where(Fix.id == fix_id)
        )
        return result.scalars().first()
    
    async def list_by_issue(self, issue_id: int) -> list[Fix]:
        result = await self.session.execute(
            select(Fix).order_by(Fix.id.desc())
        )
        return result.scalars().all()
