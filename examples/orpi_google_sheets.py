import logging

from immosheets import (RealEstate, OrpiService, OrpiSearchQuery,
                        OrpiLocation, OrpiRealEstateType, OrpiRealEstateFilter,
                        OrpiLayoutType, GoogleSpreadsheetsService)


SHEET_ID: str = ""

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    orpi = OrpiService()
    google_sheets = GoogleSpreadsheetsService(
        credentials_file_path='./credentials.json')

    rouen = OrpiLocation(label="Rouen+(76000)", value="rouen")

    query = OrpiSearchQuery(
        locations=[rouen],
        layoutType=OrpiLayoutType.MIXTE,
        maxPrice=800,
        minSurface=40,
        realEstateTypes=[OrpiRealEstateType.APPARTMENT],
        sort=OrpiRealEstateFilter.NEWEST,
        recentlySold=False
    )

    google_sheets.use(SHEET_ID).clear().add_headers()
    results: RealEstate = orpi.search(query)
    google_sheets.insert(results)
