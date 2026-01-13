from utils import query_duckdb

if __name__ == "__main__":
    query_duckdb("""
    CREATE TABLE IF NOT EXISTS restaurants (
        name TEXT,
        type_of_food TEXT, 
        price INTEGER, 
        rating INTEGER, 
        description TEXT, 
        opening_hours TEXT, 
        location TEXT
    )
    """)