from abc import ABC, abstractmethod
from typing import List

from seloger_google_sheets.real_estate import RealEstate
from seloger_google_sheets.search_query import SearchQuery

class RealEstateService(ABC):
    @abstractmethod
    def search(self, query: SearchQuery) -> List[RealEstate]:
        """ Will communicate with an external service to retrive data based on a global search query.
        
        This is meant to be inherited for integration purposes.
        """ 
