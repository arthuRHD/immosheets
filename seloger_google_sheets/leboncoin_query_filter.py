from pydantic import BaseModel

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

class Area(BaseModel):
    lat: float
    lng: float
    default_radius: int = 5000
    radius: int

class Location(BaseModel):
    locationType: str
    label: str
    city: str
    department_id: str
    region_id: str
    area: Area

class LeboncoinLocations(BaseModel):
    locations: list[Location] = []

class Range(BaseModel):
    min: int | None
    max: int | None

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
