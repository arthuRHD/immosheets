import logging

from immosheets import (SelogerService, SelogerSearchQuery, SelogerRealEstateFilter, 
SelogerRealEstateType, SelogerTransactionType, GoogleSpreadsheetsService)


API_KEY: str = ""
SHEET_ID: str = ""

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    seloger = SelogerService(api_key=API_KEY)
    google_sheets = GoogleSpreadsheetsService(credentials_file_path='./credentials.json')

    query = SelogerSearchQuery(
        maximumPrice="800",
        zipCodes="76300,76800,76000",
        includeNewConstructions="false",
        transactionType=SelogerTransactionType.RENT,
        realtyTypes=SelogerRealEstateType.APPARTMENT,
        sortBy=SelogerRealEstateFilter.NEWEST
    )

    google_sheets.use(SHEET_ID).clear().add_headers()

    for result in seloger.search(query):
        google_sheets.insert(result)
        