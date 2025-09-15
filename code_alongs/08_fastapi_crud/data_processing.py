from constants import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field, field_validator

def read_json(filename: str):
    with open(DATA_PATH / filename, "r") as file:
        data = json.read(file)
    return data

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(gt = 1500, lt = 2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 11,
                "title": "Learn with AIgineer",
                "author": "Kokchun Giang",
                "year": 2025
            }
        } 
    }

class Library(BaseModel):
    name: str
    books: list[Book]


def library_data(filename):
    # deserializes library json data into a library model
    json_data = read_json(filename)
    return Library.model_validate(json_data)

class YearFilter(BaseModel):
    start_year: int = Field(1800, gt=1000, lt=2026)
    end_year: int = Field(2000, gt=1000, lt=2026)

    @field_validator("end_year")
    @classmethod
    def validate_end_year(cls, value, info):
        if value <= info.data.get("start_year"):
            raise ValueError("End_year must greater than start_year")
        return value

if __name__ == "__main__":
    data = library_data("../../data/library.json")
    print(data)