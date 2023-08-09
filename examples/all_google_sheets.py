import logging

from immosheets import (SelogerService, OrpiService, OrpiSearchQuery,
                        OrpiLocation, OrpiRealEstateType, OrpiRealEstateFilter,
                        OrpiLayoutType, SelogerSearchQuery, SelogerRealEstateFilter,
                        SelogerRealEstateType, SelogerTransactionType, GoogleSpreadsheetsService)


API_KEY: str = ""
SHEET_ID: str = ""

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    seloger = SelogerService(api_key=API_KEY)
    orpi = OrpiService()
    google_sheets = GoogleSpreadsheetsService(
        credentials_file_path='./credentials.json')

    seloger_query = SelogerSearchQuery(
        maximumPrice="800",
        zip_codes="76300,76800,76000",
        includeNewConstructions="false",
        transactionType=SelogerTransactionType.RENT,
        realtyTypes=SelogerRealEstateType.APPARTMENT,
        sortBy=SelogerRealEstateFilter.NEWEST
    )

    rouen = OrpiLocation(label="Rouen+(76000)", value="rouen")

    orpi_query = OrpiSearchQuery(
        locations=[rouen],
        layoutType=OrpiLayoutType.MIXTE,
        maxPrice=800,
        minSurface=40,
        realEstateTypes=[OrpiRealEstateType.APPARTMENT],
        sort=OrpiRealEstateFilter.NEWEST,
        recentlySold=False
    )

    google_sheets.use(SHEET_ID).clear().add_headers()

    for result in seloger.search(seloger_query):
        google_sheets.insert(result)

    google_sheets.insert(orpi.search(orpi_query))
