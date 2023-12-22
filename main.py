from fastapi import FastAPI
from app import models
from app.database import engine
from app import endpoints

app = FastAPI()

models.Base.metadata.create_all(engine)


"""
@app.get("/")
def test():
    return {"test": "data"}


@app.get("/data/{id}")
def test_id(id: int):
    return {"data": id}

"""

app.include_router(endpoints.router)
