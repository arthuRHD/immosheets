import attr
from typing import Optional
from ..settings import settings


def _validate_greater_than_zero_int(instance, attribute, value: str | None):
    if value is not None:
        try:
            numeric_value = int(value)
            if numeric_value <= 0:
                raise ValueError(f"{attribute.name} must be greater than 0")
        except ValueError:
            raise ValueError(f"{attribute.name} must be a valid integer string")

def _validate_greater_than_zero_float(instance, attribute, value: str | None):
    if value is not None:
        try:
            numeric_value = float(value)
            if numeric_value <= 0:
                raise ValueError(f"{attribute.name} must be greater than 0")
        except ValueError:
            raise ValueError(f"{attribute.name} must be a valid numeric string")


def _validate_is_boolean_string(instance, attribute, value: str | None):
    if value is not None and value not in ["true", "false"]:
        raise ValueError(f"{attribute.name} must be 'true' or 'false'")

def _validate_min_one_bedroom_or_room(instance, attribute, value: str | None):
    if value is not None:
        try:
            num = int(value)
            if num < 1:
                raise ValueError(f"{attribute.name} must be at least 1")
        except ValueError:
            raise ValueError(f"{attribute.name} must be a valid integer string")

def _validate_zipcodes(instance, attribute, value: str):
    separator: str = ","

    if not value:
        raise ValueError("zipCodes must have at least one zipcode")

    if separator in value:
        for code in value.split(separator):
            if not code.isdigit():
                raise ValueError(f"'{code}' in {attribute.name} are not digits")
    else:
        if not value.isdigit():
            raise ValueError(f"'{value}' in {attribute.name} are not digits")


@attr.s(auto_attribs=True, frozen=True)
class SelogerSearchQuery:
    zipCodes: str = attr.field(validator=_validate_zipcodes)
    maximumPrice: Optional[str] = attr.field(default=None, validator=_validate_greater_than_zero_int)
    minimumPrice: Optional[str] = None
    maximumFloor: Optional[str] = None
    minimumFloor: Optional[str] = attr.field(default=None, validator=_validate_greater_than_zero_int)
    maximumLivingArea: Optional[str] = None
    minimumLivingArea: Optional[str] = attr.field(default=None, validator=_validate_greater_than_zero_float)
    bedrooms: Optional[str] = attr.field(default=None, validator=_validate_min_one_bedroom_or_room)
    rooms: Optional[str] = attr.field(default=None, validator=_validate_min_one_bedroom_or_room)
    districtIds: Optional[str] = None
    pageSize: str = attr.field(default=settings.page_size)
    pageIndex: str = attr.field(default="1")
    includeNewConstructions: Optional[str] = attr.field(default=None, validator=_validate_is_boolean_string)
    transactionType: Optional[str] = None
    realtyTypes: Optional[str] = None
    sortBy: Optional[str] = None
