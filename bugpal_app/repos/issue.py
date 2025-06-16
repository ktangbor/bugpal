from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from bugpal_app.models.issue import Issue
from bugpal_app.api.v1.schemas.issue import IssueCreate

class IssueRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, issue: IssueCreate, user_id: int) -> Issue:
        issue_db = Issue(**issue.model_dump(), user_id=user_id)
        self.session.add(issue_db)
        await self.session.flush()
        return issue_db

    async def get(self, issue_id: int) -> Issue|None:
        result = await self.session.execute(
            select(Issue).where(Issue.id == issue_id)
        )
        return result.scalars().first()

    async def list_all(self) -> list[Issue]:
        result = await self.session.execute(
            select(Issue).order_by(Issue.id.desc())
        )
        return result.scalars().all()
