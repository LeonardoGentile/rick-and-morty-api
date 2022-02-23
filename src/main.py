from fastapi import FastAPI

from src.database import engine
from . import models
from .api.router import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Pickle Rick!!"}

