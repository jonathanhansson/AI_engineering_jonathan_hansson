from pydantic import BaseModel, Field

class Restaurant(BaseModel):
    name: str
    type_of_food: str
    price: int = Field(lt=4, gt=0, description="This is the price of the food between 1 and 3. 3 means 200kr+ for a meal, 2 means 100-200kr for a meal, 1 means under 100kr for a meal.")
    rating: int = Field(lt=6, gt=0, description="Overall rating of the restaurant between 1 (bad) and 5 (excellent)")
    description: str
    opening_hours: str = Field(description="Using swedish time (not AM and PM). E.g. '07:00-12:00'")
    location: str = Field(description="Name the street address.")


class Prompt(BaseModel):
    prompt: str