from pydantic import BaseModel
from ..location import Location
from ..range import Range

class LeboncoinCategory(BaseModel):
    id: int

class LeboncoinEnums(BaseModel):
    ad_type: list = ["offer"]
    real_estate_type: list = ["2"]
    furnished: list = list[str] | None
    energy_rate: list[str] | None

class LeboncoinKeywords(BaseModel):
    text: str | None
    parrot_used: int | None

class LeboncoinLocations(BaseModel):
    locations: list[Location] = []

class LeboncoinRanges(BaseModel):
    land_plot_surface: Range | None
    price: Range | None
    rooms: Range | None
    square: Range | None

class LeboncoinQueryFilter(BaseModel):
    category: LeboncoinCategory
    enums: LeboncoinEnums
    keywords: LeboncoinKeywords
    location: LeboncoinLocations
    range: LeboncoinRanges | dict = {}
