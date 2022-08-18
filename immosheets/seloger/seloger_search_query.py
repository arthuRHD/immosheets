from pydantic import BaseModel, validator
from ..settings import settings


class SelogerSearchQuery(BaseModel):
    zipCodes: str
    maximumPrice: str | None
    minimumPrice: str | None
    maximumFloor: str | None
    minimumFloor: str | None
    maximumLivingArea: str | None
    minimumLivingArea: str | None
    bedrooms: str | None
    rooms: str | None
    districtIds: str | None
    pageSize: str = settings.page_size
    pageIndex: str = "1"
    includeNewConstructions: str | None
    transactionType: str | None
    realtyTypes: str | None
    sortBy: str | None

    @validator('maximumPrice')
    def price_is_greater_than_zero(cls, price: str | None):
        if price is not None:
            assert int(price) > 0, "maximumPrice is lesser then 0"
        return price

    @validator('minimumFloor')
    def floor_is_greater_than_zero(cls, floor: str | None):
        if floor is not None:
            assert int(floor) > 0, "minimumFloor is lesser then 0"
        return floor

    @validator('minimumLivingArea')
    def living_area_is_greater_than_zero(cls, living_area: str | None):
        if living_area is not None:
            assert float(living_area) > 0, "minimumPrice is lesser then 0"
        return living_area

    @validator("includeNewConstructions")
    def is_boolean(cls, include: str | None):
        if include is not None:
            assert include in ["true", "false"], "includeNewConstructions is not a boolean"
        return include

    @validator("bedrooms")
    def must_have_at_least_one_bedroom(cls, bedroom: str | None):
        if bedroom is not None:
            assert int(bedroom) > 1, "must have at least one bedroom"
        return bedroom

    @validator("rooms")
    def must_have_at_least_one_room(cls, room: str | None):
        if room is not None:
            assert int(room) > 1, "must have at least one room"
        return room

    @validator("zipCodes")
    def zipcodes_validator(cls, zipcodes: str):
        separator: str = ","

        assert zipcodes != "", "must have at least one zipcode" 

        if separator in zipcodes:
            for code in zipcodes.split(separator):
                assert code.isdigit(), f"{code} are not digits"
        assert zipcodes.isdigit(), f"{zipcodes} are not digits"

        return zipcodes