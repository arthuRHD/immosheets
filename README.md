<div id="header" align="center">
  <img src="SVGLogo.svg"/><br><br>
    <p><strong><em>Tired of searching with your mouse ? Let's automate the process.</em></strong></p>
    <a href="https://app.codacy.com/project/badge/Grade/ba1afb9f8ffe402ca6a31a30ba63b628">
      <img src="https://app.codacy.com/project/badge/Grade/ba1afb9f8ffe402ca6a31a30ba63b628" alt="Codacy Badge">
   </a>
   <a href="https://badge.fury.io/py/immosheets">
      <img src="https://badge.fury.io/py/immosheets.svg" alt="PyPI version">
  </a>
  <a href="https://pepy.tech/project/immosheets">
     <img src="https://static.pepy.tech/badge/immosheets" alt="Downloads">
  </a>
  <a href="https://github.com/arthuRHD/immosheets/actions/workflows/python-publish.yml">
    <img src="https://github.com/arthuRHD/immosheets/actions/workflows/python-publish.yml/badge.svg" alt="release">
  </a>
  <a href="https://github.com/arthuRHD/immosheets/actions/workflows/documentation-publish.yml">
    <img src="https://github.com/arthuRHD/immosheets/actions/workflows/documentation-publish.yml/badge.svg" alt="documentation">
  </a>
</div>
<br>

## Description :
+ Introducing "**immosheets**", a tool that streamlines your search process by automating it. 
+ No more tedious mouse clicking and scrolling through search results. With **immosheets**, you can quickly and easily find what you're looking for with just a few simple commands. 
+ Whether you're a developer looking for code snippets or a researcher scouring the web for information, **immosheets** can help you save time and increase your productivity. 

<div align="center">
<h3>Try immosheets out today and see the difference for yourself!<h3>
</div>



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

google_sheets.use("my_sheet_id").clear().add_headers()

for result in seloger.search(query):
    google_sheets.insert(result)
```
## Genereting credentials

| **Third party** | **Instructions**                                                                                                                                                                                                                                                                                                                     |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [<img src="https://kstatic.googleusercontent.com/files/adf55cdf4c7f8fb38efbf8df6c2792660fbeff2d05be05f2ec8e9c265a179b51c64b9679d8aee00e09cad19ce419d90a2d999b82cea4200abbe78c73e6bfaacf" width=100>](https://www.google.fr/intl/fr/sheets/about/)    | To learn how to create credentials, go to [Create credentials](https://developers.google.com/workspace/guides/create-credentials).  Once you create the credentials, make sure the downloaded JSON file is saved as credentials.json. Then move the file to your working directory and fill the path when instanciating the service. |
| [<img src="https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/bf/64/69/bf646951-e676-9162-1300-4e9a3beb1a8f/AppIcon-0-1x_U007emarketing-0-7-0-85-220.png/256x256bb.jpg" width=100>](https://www.seloger.com/)        | Generate your API key [here](https://rapidapi.com/apidojo/api/seloger/). An account on RapidAPI is needed to retrieve an API key. |
| [<img src="https://static.orpi.com/images/orpibackend/default/5c6e83b340014_Orpi_picto_Agences%20ORPI_ROUGE.png" width=100>](https://www.orpi.com/) | Nothing to do. |
|  [<img src="https://www.erafrance.com/assets/imgs/era-logo-national.svg" width=100>](https://www.erafrance.com) | Work in progress. |
| [<img src="https://www.ouestfrance-immo.com/photo-laforet-guingamp/client/1498/laforet-guingamp-1498logo.jpg" width=100>](https://www.laforet.com/) | Work in progress. |

Check out examples for more.

## For contributors

To install development dependencies

```sh
pip install -r requirements.txt
```

To install the package locally with your new code inside

```sh
pip install -e .
```

There are no unit tests or documentation currently, we're working on that.

## Integration

+ At this time, I am able to integrate with seloger.com and Google Sheets.
+ I am currently in the process of implementing support for Leboncoin.
+ If you would like me to integrate with any other third-party platforms, please submit a request in the form of an issue.
+ Additional integrations beyond seloger.com and Google Sheets are being considered and are open for request through the creation of an issue.
+ Your suggestions will be taken into consideration and evaluated for feasibility and compatibility with my current system.
+ We appreciate your feedback and suggestions as it helps us to improve and expand my capabilities to better serve you!

### You can actually write your own integration based on defaults abstract classes located at the root of the package :

- 'RealEstateService' for data acquisition
- 'ReportingService' to display and manage data
    
    
### Integration Ideas 
    
Here's few integrations ideas:

- Excel
- MongoDB
- MySQL
- ElasticSearch
- Persist data as a File (JSON, XML, CSV)
- Explorimmo
- meilleursagents.com
- apimo.net
