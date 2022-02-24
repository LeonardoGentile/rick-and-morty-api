from fastapi import FastAPI

from src.database import init_db
from .api.router import api_router

init_db()

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Pickle Rick!!"}

