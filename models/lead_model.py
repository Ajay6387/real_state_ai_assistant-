from pydantic import BaseModel
from typing import Optional

class Lead(BaseModel):
    intent: str               # BUY or SELL
    name: str
    location: str
    phone: str
    email: str
    budget: Optional[float] = None
    postcode: Optional[str] = None
    home_type: Optional[str] = None
