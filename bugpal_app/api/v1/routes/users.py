from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from bugpal_app.depedencies import get_async_session
from bugpal_app.api.v1.schemas.user import UserCreate
from bugpal_app.services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create")
async def create_user(user: UserCreate,
                      session: AsyncSession = Depends(get_async_session)):
    service = UserService(session)
    return service.create_user(user)
