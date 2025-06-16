from sqlalchemy.ext.asyncio import AsyncSession
from bugpal_app.db.session import AsyncSessionLocal
from collections.abc import AsyncGenerator


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
