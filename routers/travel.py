import os

from dotenv import dotenv_values
from fastapi import APIRouter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
import sqlite3

from models.travel import Travel

router = APIRouter(tags=["travel"])

config = dotenv_values(".env")

@router.post("/travel")
async def should_travel(travel: Travel) -> None:
    """
        Given a source and destination, return whether the user should travel or not.
        based on if the destination is hotter than the source.

        Args:
            travel (Travel): source and destination
        
        Returns:
            str: whether the user should travel or not.
    """

    source = travel.source
    destination = travel.destination

    # Set the OpenAI API key
    os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]

    # Create the OpenAI chatbot
    llm = ChatOpenAI(temperature=0)

    # Define the prompt
    prompt = PromptTemplate.from_template(
        """
        Write Exactly two SQl queries to get the temperature of the source and destination.

        Query1: SELECT temperature FROM weather WHERE name = {source};
        Query2: SELECT temperature FROM weather WHERE name = {destination};

        return the output in the following format:
        (Query1, Query2)
        """
    )

    # Create the Prompt Flow
    runnable = prompt | llm | StrOutputParser()

    # Run the Prompt Flow
    result = runnable.invoke({"source": source, "destination": destination})


