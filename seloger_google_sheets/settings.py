from pydantic import BaseSettings

class Settings(BaseSettings):
    seloger_url: str = 'https://seloger.p.rapidapi.com/properties/list'
    google_api_scope: str = 'https://www.googleapis.com/auth/spreadsheets'
    google_sheets_range_name: str = 'A1:J'
    rapidapi_host: str = 'seloger.p.rapidapi.com'
    page_size: str = "700"
    
settings = Settings()
