from typing import Optional
from .settings import settings
from .search_query import SearchQuery


class SelogerSearchQuery(SearchQuery):
    zipCodes: str
    pageSize: str = settings.page_size
    pageIndex: str = "1"
    includeNewConstructions: Optional[str]
    transactionType: Optional[str]
    realtyTypes: Optional[str]
    sortBy: Optional[str]
