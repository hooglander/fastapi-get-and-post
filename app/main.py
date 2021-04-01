from fastapi import FastAPI
from . import models, routers
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(routers.router)