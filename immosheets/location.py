import attr
from .area import Area

@attr.s(auto_attribs=True)
class Location:
    locationType: str
    label: str
    city: str
    department_id: str
    region_id: str
    area: Area
