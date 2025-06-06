import attr
from environ import to_config, var

@attr.s(auto_attribs=True, frozen=True)
class Settings:
    seloger_url: str = var("SELOGER_URL", default='https://seloger.p.rapidapi.com/properties/list')
    leboncoin_url: str = var("LEBONCOIN_URL", default='https://leboncoin1.p.rapidapi.com/v2/leboncoin/search_api')
    era_url: str = var("ERA_URL", default='https://api.erafrance.com/api')
    orpi_url: str = var("ORPI_URL", default='https://www.orpi.com/recherche/ajax')
    google_api_scope: str = var("GOOGLE_API_SCOPE", default='https://www.googleapis.com/auth/spreadsheets')
    google_sheets_range_name: str = var("GOOGLE_SHEETS_RANGE_NAME", default='A1:K')
    seloger_host: str = var("SELOGER_HOST", default='seloger.p.rapidapi.com')
    leboncoin_host: str = var("LEBONCOIN_HOST", default='leboncoin1.p.rapidapi.com')
    page_size: str = var("PAGE_SIZE", default="50")
    request_timeout_in_secs: int = var("REQUEST_TIMEOUT_IN_SECS", default=30)

settings = to_config(Settings)