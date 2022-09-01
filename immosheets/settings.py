from pydantic import BaseSettings

class Settings(BaseSettings):
    seloger_url: str = 'https://seloger.p.rapidapi.com/properties/list'
    leboncoin_url: str = 'https://leboncoin1.p.rapidapi.com/v2/leboncoin/search_api'
    google_api_scope: str = 'https://www.googleapis.com/auth/spreadsheets'
    google_sheets_range_name: str = 'A1:J'
    seloger_host: str = 'seloger.p.rapidapi.com'
    leboncoin_host: str = 'leboncoin1.p.rapidapi.com'
    page_size: str = "50"
    
settings = Settings()
