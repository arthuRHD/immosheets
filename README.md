<img src="https://github.com/arthuRHD/immosheets/blob/6222c6bb6e1f80fb8de2a60368aeb918207c4adb/SVGLogo.svg"/>

Tired of searching with your mouse ? Let's automate the process.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ba1afb9f8ffe402ca6a31a30ba63b628)](https://www.codacy.com/gh/arthuRHD/immosheets/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=arthuRHD/immosheets&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/immosheets.svg)](https://badge.fury.io/py/immosheets)
[![Downloads](https://static.pepy.tech/badge/immosheets)](https://pepy.tech/project/immosheets)

## Usage

### Install

```sh
pip install immosheets
```

### Write your script

This is meant to be used as a package for your bot.

```py
from immosheets import (SelogerService, SelogerSearchQuery, SelogerRealEstateFilter, 
SelogerRealEstateType, SelogerTransactionType, GoogleSpreadsheetsService)


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
    google_sheets.insert(result)
```
## Genereting credentials

| **Third party** | **Instructions**                                                                                                                                                                                                                                                                                                                     |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [<img src="https://kstatic.googleusercontent.com/files/adf55cdf4c7f8fb38efbf8df6c2792660fbeff2d05be05f2ec8e9c265a179b51c64b9679d8aee00e09cad19ce419d90a2d999b82cea4200abbe78c73e6bfaacf" width=100>](https://www.google.fr/intl/fr/sheets/about/)    | To learn how to create credentials, go to [Create credentials](https://developers.google.com/workspace/guides/create-credentials).  Once you create the credentials, make sure the downloaded JSON file is saved as credentials.json. Then move the file to your working directory and fill the path when instanciating the service. |
| [<img src="https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/bf/64/69/bf646951-e676-9162-1300-4e9a3beb1a8f/AppIcon-0-1x_U007emarketing-0-7-0-85-220.png/256x256bb.jpg" width=100>](https://www.seloger.com/)        | Generate your API key [here](https://rapidapi.com/apidojo/api/seloger/). An account on RapidAPI is needed to retrieve an API key. |
| [<img src="https://static.orpi.com/images/orpibackend/default/5c6e83b340014_Orpi_picto_Agences%20ORPI_ROUGE.png" width=100>](https://www.orpi.com/) | Nothing to do. |
|  [<img src="https://www.erafrance.com/assets/imgs/era-logo-national.svg" width=100>](https://www.erafrance.com) | Nothing to do. |
| [<img src="https://www.ouestfrance-immo.com/photo-laforet-guingamp/client/1498/laforet-guingamp-1498logo.jpg" width=100>](https://www.laforet.com/) | Nothing to do. |

Check out examples for more.

### Do your own integration

I'm currently only supporting seloger.com and google sheets as third parties. I'm working on Leboncoin integration. For other integrations, feel free to write an issue.

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
