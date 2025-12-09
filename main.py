from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import EmailStr, BaseModel
from items_views import router as items_router
from users.views import router as users_router
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from core.config import settings
from api_v1 import router as api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(api_v1_router, prefix=settings.api_v1_prefix)


