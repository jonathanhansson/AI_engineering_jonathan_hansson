from fastapi import FastAPI
from data_models import Restaurant, Prompt
from agents import restaurant_agent
from utils import query_duckdb

app = FastAPI()

@app.get("/show_table")
async def show_restaurants():
    restaurants = query_duckdb("SELECT * FROM restaurants", parameters=[])

    return restaurants.to_dict(orient="records")

@app.post("/restaurant_recommendation")
async def recommend_restaurant(query: Prompt):
    result = await restaurant_agent.run(query.prompt)

    restaurant = result.output

    query_duckdb(
        """
        INSERT INTO restaurants (
            name, 
            type_of_food, 
            price, 
            rating, 
            description, 
            opening_hours, 
            location
        ) 
        VALUES (
            ?, ?, ?, ?, ?, ?, ?
        )
        """,
        parameters=[
            restaurant.name,
            restaurant.type_of_food,
            restaurant.price,
            restaurant.rating,
            restaurant.description,
            restaurant.opening_hours,
            restaurant.location
        ]
    )

    return restaurant.model_dump()