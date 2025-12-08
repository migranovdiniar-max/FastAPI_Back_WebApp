from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import EmailStr, BaseModel
from items_views import router as items_router
from users.views import router as users_router


app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)