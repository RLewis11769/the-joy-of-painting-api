from pydantic import BaseModel
from typing import Optional

# Object structure for post requests
class Add_Episode(BaseModel):
    """ Episode Model """
    title: str
    date: str

# Object structure for put requests
class Update_Episode(BaseModel):
    """ Episode Model """
    title: Optional[str] = None
    date: Optional[str] = None
