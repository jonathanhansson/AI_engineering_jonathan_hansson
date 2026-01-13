from pydantic_ai import Agent
from dotenv import load_dotenv
from data_models import Restaurant

load_dotenv()

restaurant_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    system_prompt=
    """
    You will receive a location prompt (e.g. Avenyn Göteborg). You should generate a restaurant in that location.
    """,
    output_type=Restaurant
)