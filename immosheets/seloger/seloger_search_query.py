from pydantic import field_validator, BaseModel
from ..settings import settings


class SelogerSearchQuery(BaseModel):
    zip_codes: str
    maximumPrice: str | None = None
    minimumPrice: str | None = None
    maximumFloor: str | None = None
    minimumFloor: str | None = None
    maximumLivingArea: str | None = None
    minimumLivingArea: str | None = None
    bedrooms: str | None = None
    rooms: str | None = None
    districtIds: str | None = None
    pageSize: str = settings.page_size
    pageIndex: str = "1"
    includeNewConstructions: str | None = None
    transactionType: str | None = None
    realtyTypes: str | None = None
    sortBy: str | None = None

    @field_validator('maximumPrice')
    @classmethod
    def price_is_greater_than_zero(cls, price: str | None):
        if price is not None:
            if int(price) <= 0:
                raise ValueError("maximumPrice is lesser then or equals 0")
        return price

    @field_validator('minimumFloor')
    @classmethod
    def floor_is_greater_than_zero(cls, floor: str | None):
        if floor is not None:
            if int(floor) <= 0:
                raise ValueError("minimumFloor is lesser then or equals 0")
        return floor

    @field_validator('minimumLivingArea')
    @classmethod
    def living_area_is_greater_than_zero(cls, living_area: str | None):
        if living_area is not None:
            if float(floor) <= 0:
                raise ValueError("living area is lesser then or equals 0")
        return living_area

    @field_validator("includeNewConstructions")
    @classmethod
    def is_boolean(cls, include: str | None):
        if include is not None:
            if include not in ["true", "false"]:
                raise ValueError("includeNewConstructions is not a boolean")
        return include

    @field_validator("bedrooms")
    @classmethod
    def must_have_at_least_one_bedroom(cls, bedroom: str | None):
        if bedroom is not None:
            if int(bedroom) < 1: raise ValueError("must have at least one bedroom")
        return bedroom

    @field_validator("rooms")
    @classmethod
    def must_have_at_least_one_room(cls, room: str | None):
        if room is not None:
            if int(room) < 1: raise ValueError("must have at least one room")
        return room

    @field_validator('zip_codes')
    @classmethod
    def postal_code_is_correct(cls, zip_codes: str | None):
        separator: str = ","

        if zip_codes == "": raise ValueError("must have at least one zipcode")

        if separator in zip_codes:
            for code in zip_codes.split(separator):
                if not code.isdigit(): raise ValueError(f"{code} are not digits")
        else:
            if not zip_codes.isdigit(): raise ValueError(f"{zip_codes} are not digits")

        return zip_codes
