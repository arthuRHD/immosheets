from abc import ABC, abstractmethod

from .real_estate import RealEstate
from pydantic import BaseModel

class RealEstateService(ABC):
    @abstractmethod
    def search(self, query: BaseModel) -> list[RealEstate]:
        """ Will communicate with an external service to retrive data based on a global search query.
        
        This is meant to be inherited for integration purposes.
        """ 
