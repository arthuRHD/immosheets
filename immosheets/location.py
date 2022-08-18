from pydantic import BaseModel
from .area import Area

class Location(BaseModel):
    locationType: str
    label: str
    city: str
    department_id: str
    region_id: str
    area: Area