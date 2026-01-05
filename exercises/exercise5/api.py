from fastapi import FastAPI, Query
from data_processing import Iris

app = FastAPI()

@app.get("/iris")
def read_flowers(limit: int = Query(100, gt=0, lt=151)):
    iris = Iris(limit)
    return iris.to_json()

@app.get("/iris/species/")
def filter_flowers(flower: str):
    iris = Iris()
    return iris.filter_flower(flower).to_json()

