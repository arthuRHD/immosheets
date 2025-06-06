import attr
from typing import List, Optional, Union

from immosheets.orpi.orpi_transaction_type import OrpiTransactionType


class OrpiRealEstateType:
    HOUSE: str = "maison"
    APPARTMENT: str = "appartement"


class OrpiRealEstateFilter:
    NEWEST: str = "date-down"


class OrpiLayoutType:
    MIXTE: str = "mixte"


@attr.s(auto_attribs=True, frozen=True)
class OrpiLocation:
    label: str
    value: str


@attr.s(auto_attribs=True, frozen=True)
class OrpiSearchQuery:
    transactionType: str = attr.field(default=OrpiTransactionType.RENT)
    realEstateTypes: List[str] = attr.field()
    locations: List[OrpiLocation] = attr.field()
    sort: Optional[str] = attr.field(default=OrpiRealEstateFilter.NEWEST)
    layoutType: Optional[str] = attr.field(default=OrpiLayoutType.MIXTE)
    maxPrice: Optional[int] = None
    minPrice: Optional[int] = None
    maxSurface: Optional[int] = None
    minSurface: Optional[int] = None
    recentlySold: bool = attr.field(default=False)

    def parse_real_estate_types(self) -> str:
        url_path: str = ""
        for real_estate_type in self.realEstateTypes:
            url_path += f"realEstateTypes[]={real_estate_type}&"
        return url_path

    def parse_locations(self) -> str:
        url_path: str = ""
        for i, location in enumerate(self.locations):
            url_path += f"locations[{i}][label]={location.label}&"
            url_path += f"locations[{i}][value]={location.value}&"
        return url_path

    def parse_transaction_type(self) -> str:
        return f"/{self.transactionType}?"
