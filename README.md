# immosheets

Tired of searching with your mouse ? Let's automate the process.

This is meant to be used as a package for your bot.

I'm currently only supporting seloger.com and google sheets as third parties. I'm working on Leboncoin integration. For other integrations, feel free to write an issue.

## Genereting credentials

### Google sheets

To learn how to create credentials, go to [Create credentials](https://developers.google.com/workspace/guides/create-credentials).

Once you create the credentials, make sure the downloaded JSON file is saved as credentials.json. Then move the file to your working directory and fill the path when instanciating the service.

### SeLoger

An account on *RapidAPI* is needed to retrieve an API key.

[https://rapidapi.com/apidojo/api/seloger/](https://rapidapi.com/apidojo/api/seloger/)

## Usage

### Install

```sh
pip install immosheets
```

### Write your script

```py
from immosheets import (SelogerService, SelogerSearchQuery, SelogerRealEstateFilter, 
SelogerRealEstateType, SelogerTransactionType, RealEstate, GoogleSpreadsheetsService)


seloger = SelogerService(api_key='my_seloger_api_key')
google_sheets = GoogleSpreadsheetsService(credentials_file_path='./credentials.json')

query = SelogerSearchQuery(
    maximumPrice="800",
    zipCodes="76300,76800,76000",
    includeNewConstructions="false",
    transactionType=SelogerTransactionType.RENT,
    realtyTypes=SelogerRealEstateType.APPARTMENT,
    sortBy=SelogerRealEstateFilter.NEWEST
)

google_sheets.use("my_sheet_id").clear()

for result in seloger.search(query):
    google_sheets.insert(result
```

### Do your own integration

You can actually write your own integration based on defaults abstract classes located at the root of the package.

- 'RealEstateService' for data acquisition
- 'ReportingService' to display and manage data

Here's few integrations ideas:

- Excel
- MongoDB
- MySQL
- ElasticSearch
- Persist data as a File (JSON, XML, CSV)
- Explorimmo
- meilleursagents.com
- apimo.net
