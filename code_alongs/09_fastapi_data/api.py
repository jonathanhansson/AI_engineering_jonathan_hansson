from fastapi import FastAPI
from data_processing import DataExplorer
import pandas as pd

app = FastAPI()

data_explorer = DataExplorer(limit=50)

@app.get("/api/sales")
async def read_sales():
    # Implement this
    """Returns sales data as JSON"""
    return data_explorer.json_response()

@app.get("/api/sales/summary")
async def read_summary_data():
    """ shows summary stats """
    return data_explorer.summary().json_response()

@app.get("/api/sales/kpis")
async def read_kpis(country: str):
    # KPI:s based on countries
    return data_explorer.kpis(country=country)

# to run the api
# uvicorn api:app --reload

# navigate to /docs for swagger UI