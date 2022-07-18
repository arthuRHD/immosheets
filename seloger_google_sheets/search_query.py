from typing import Optional
from pydantic import BaseModel

    
class SearchQuery(BaseModel):
    """Basic search query object, meant to be inherited for integrations purposes
    """    
    maximumPrice: Optional[str]
    bedrooms: Optional[str]