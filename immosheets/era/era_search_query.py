import attr
from typing import List, Optional, Any
from .utils import create_attrs_instance_from_dict

@attr.s(auto_attribs=True, frozen=True)
class EraSearchQuery:
    page_size: int = attr.field(default=1000, metadata={'alias': 'per_page'})
    distance: int = attr.field(default=0)
    real_estate_type: Optional[List[str]] = attr.field(default=None, metadata={'alias': 'type_bien'})
    transaction_type: str = attr.field(metadata={'alias': 'annonce_type'}) # Required, no default
    transaction_type_bis: Optional[str] = attr.field(default=None, metadata={'alias': 'type_annonce'})
    location_id: Optional[str] = attr.field(default=None, metadata={'alias': 'geo_ville_id'})
    min_square_meter: int = attr.field(default=1, metadata={'alias': 'surface_from'})
    max_square_meter: Optional[int] = attr.field(default=500, metadata={'alias': 'surface_to'}) # Was None in Pydantic, but default 500 implies not None
    min_price: int = attr.field(default=10, metadata={'alias': 'prix_from'})
    max_price: Optional[int] = attr.field(default=None, metadata={'alias': 'prix_to'})
    rooms: int = attr.field(default=1, metadata={'alias': 'nb_pieces'})
    bedrooms: int = attr.field(default=1, metadata={'alias': 'nb_chambres'})
    fields: str = attr.field(default="id")
    page: int = attr.field(default=1)
    sort_by: str = attr.field(default="desc")
    reused: bool = attr.field(default=True, metadata={'alias': 'shouldReuse'})
    format: str = attr.field(default="json", metadata={'alias': '_format'})


@attr.s(auto_attribs=True, frozen=True)
class PostalCode:
    value: Optional[str] = attr.field(default=None, validator=_validate_postal_code)


class EraTransactionType:
    RENT: str = "louer"
    BUY: str = "acheter"


class EraRealEstateType:
    HOUSE: str = "maison"
    APPARTMENT: str = "appartement"
    DUPLEX: str = "duplex"
    LAND: str = "terrain"
    OFFICE: str = "bureaux"
    COMMERCIAL: str = "local commercial,fonds de commerce,entrepôts"


def _validate_postal_code(instance, attribute, value: str | None):
    separator: str = ","

    if value is None:
        raise ValueError(f"{attribute.name} is not set")
    if value == "":
        raise ValueError(f"{attribute.name} must have at least one zipcode")

    if separator in value:
        for code in value.split(separator):
            if not code.isdigit():
                raise ValueError(f"'{code}' in {attribute.name} are not digits")
    else:
        if not value.isdigit():
            # Corrected: original Pydantic validator had `code` here, but it should be `value`
            raise ValueError(f"'{value}' in {attribute.name} are not digits")
