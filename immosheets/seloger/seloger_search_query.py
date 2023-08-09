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
            assert int(price) > 0, "maximumPrice is lesser then 0"
        return price

    @field_validator('minimumFloor')
    @classmethod
    def floor_is_greater_than_zero(cls, floor: str | None):
        if floor is not None:
            assert int(floor) > 0, "minimumFloor is lesser then 0"
        return floor

    @field_validator('minimumLivingArea')
    @classmethod
    def living_area_is_greater_than_zero(cls, living_area: str | None):
        if living_area is not None:
            assert float(living_area) > 0, "minimumPrice is lesser then 0"
        return living_area

    @field_validator("includeNewConstructions")
    @classmethod
    def is_boolean(cls, include: str | None):
        if include is not None:
            assert include in [
                "true", "false"], "includeNewConstructions is not a boolean"
        return include

    @field_validator("bedrooms")
    @classmethod
    def must_have_at_least_one_bedroom(cls, bedroom: str | None):
        if bedroom is not None:
            assert int(bedroom) > 1, "must have at least one bedroom"
        return bedroom

    @field_validator("rooms")
    @classmethod
    def must_have_at_least_one_room(cls, room: str | None):
        if room is not None:
            assert int(room) > 1, "must have at least one room"
        return room

    @field_validator('zip_codes')
    @classmethod
    def postal_code_is_correct(cls, zip_codes: str | None):
        separator: str = ","

        assert zip_codes != "", "must have at least one zipcode"

        if separator in zip_codes:
            for code in zip_codes.split(separator):
                assert code.isdigit(), f"{code} are not digits"
        else:
            assert zip_codes.isdigit(), f"{zip_codes} are not digits"

        return zip_codes
