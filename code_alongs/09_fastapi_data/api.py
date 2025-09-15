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

@app.get("/api/summary")
async def read_summary_data():
    """ shows summary stats """
    df = data_explorer.df
    total_sales = (df['Order_Quantity'] * df['Unit_Price']).sum()
    total_items_sold = df["Order_Quantity"].sum()
    avg_sale = df['Revenue'].mean()
    num_transactions = len(df)

    return {
        "total_sales_value": total_sales,
        "total_items_sold": total_items_sold,
        "average_item_price": round(avg_sale, 2),
        "number_of_transactions": num_transactions
    }


# to run the api
# uvicorn api:app --reload

# navigate to /docs for swagger UI