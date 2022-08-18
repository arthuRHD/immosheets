from pydantic import BaseModel

class Area(BaseModel):
    lat: float
    lng: float
    default_radius: int = 5000
    radius: int