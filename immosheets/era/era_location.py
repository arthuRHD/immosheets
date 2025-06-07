import attr
from typing import List, Optional
from .utils import create_attrs_instance_from_dict


@attr.s(auto_attribs=True, frozen=True)
class Town:
    id: int
    type: str
    name: str = attr.field(metadata={'alias': 'nom'})
    postal_code: str = attr.field(metadata={'alias': 'code_postal'})
    slug: str
    code: str


@attr.s(auto_attribs=True, frozen=True)
class Department:
    id: int
    name: str = attr.field(metadata={'alias': 'nom'})
    slug: str
    code: str


@attr.s(auto_attribs=True, frozen=True)
class EraLocationResponse:
    departments: Optional[List[Department]] = attr.field(default=None, metadata={'alias': 'departements'})
    towns: Optional[List[Town]] = attr.field(default=None, metadata={'alias': 'villes'})

    @classmethod
    def from_data(cls, data: dict) -> "EraLocationResponse":
        mapped_data = {}
        if 'departements' in data and data['departements'] is not None:
            mapped_data['departments'] = [create_attrs_instance_from_dict(Department, d) for d in data['departements']]
        if 'villes' in data and data['villes'] is not None:
            mapped_data['towns'] = [create_attrs_instance_from_dict(Town, t) for t in data['villes']]

        return cls(**mapped_data)


@attr.s(auto_attribs=True, frozen=True)
class EraLocationRequest:
    postal_code: str = attr.field(metadata={'alias': 'query'})
    format: str = attr.field(default="json", metadata={'alias': '_format'})
