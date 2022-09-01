from pydantic import BaseModel

class OrpiRealEstateType:
    HOUSE: str = "maison"
    APPARTMENT: str = "appartement"
    
class OrpiRealEstateFilter:
    NEWEST: str = "date-down"
    
class OrpiLayoutType:
    MIXTE: str = "mixte"
    
class OrpiLocation:
    label: str
    value: str

class OrpiSearchQuery(BaseModel):
    realEstateType: list[OrpiRealEstateType]
    locations: list[OrpiLocation]
    sort: OrpiRealEstateFilter = OrpiRealEstateFilter.NEWEST
    layoutType: OrpiLayoutType = OrpiLayoutType.MIXTE
    maxPrice: int | None
    minPrice: int | None
    maxSurface: int | None
    minSurface: int | None
    recentlySold: bool = False