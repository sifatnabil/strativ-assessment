from pydantic import BaseModel

class Travel(BaseModel):
    """
    The Travel model containing the source and destination.

    Attributes:
        source (str): The source location.
        destination (str): The destination location.
    """
    source: str
    destination: str
