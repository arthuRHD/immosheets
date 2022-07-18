from typing import Optional
from seloger_google_sheets.settings import settings
from seloger_google_sheets.search_query import SearchQuery


class SelogerSearchQuery(SearchQuery):
    zipCodes: str
    pageSize: str = settings.page_size
    pageIndex: str = "1"
    includeNewConstructions: Optional[str]
    transactionType: Optional[str]
    realtyTypes: Optional[str]
    sortBy: Optional[str]
