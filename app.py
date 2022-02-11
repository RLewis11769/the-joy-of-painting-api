from fastapi import FastAPI
from engine.db import engine, sessionmaker
# from api.v1 import episodes
from api.v1.episodes import models, views

models.Base.metadata.create_all(bind=engine)

sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()

app = FastAPI()

app.include_router(views.router)
