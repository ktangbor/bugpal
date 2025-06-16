from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (AsyncSession, create_async_engine,
                                    async_sessionmaker)
from bugpal_app.core.config import settings

engine = create_async_engine(settings.DB_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession,
                                  expire_on_commit=False, autoflush=False)

Base = declarative_base()
