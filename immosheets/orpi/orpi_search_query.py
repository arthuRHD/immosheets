from pydantic import BaseModel

from immosheets.orpi.orpi_transaction_type import OrpiTransactionType


class OrpiRealEstateType:
    HOUSE: str = "maison"
    APPARTMENT: str = "appartement"


class OrpiRealEstateFilter:
    NEWEST: str = "date-down"


class OrpiLayoutType:
    MIXTE: str = "mixte"


class OrpiLocation(BaseModel):
    label: str
    value: str


class OrpiSearchQuery(BaseModel):
    transactionType: str = OrpiTransactionType.RENT
    realEstateTypes: list[str]
    locations: list[OrpiLocation]
    sort: str | None = OrpiRealEstateFilter.NEWEST
    layoutType: str | None = OrpiLayoutType.MIXTE
    maxPrice: int | None = None
    minPrice: int | None = None
    maxSurface: int | None = None
    minSurface: int | None = None
    recentlySold: bool = False

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
