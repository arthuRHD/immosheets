from pydantic import BaseModel
from .leboncoin_query_filter import LeboncoinQueryFilter

class LeboncoinSearchQuery(BaseModel):
    sort_order: str = "desc"
    limit: int = 0
    listing_source: str = "direct-search"
    extend: bool = True
    filters: LeboncoinQueryFilter
    offset: int = 0
    limit_alu: int = 0