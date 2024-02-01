from typing import Union

from fastapi import FastAPI
from users.views import router as user_router

app = FastAPI()

# uvicorn main:app --reload
app.include_router(user_router)