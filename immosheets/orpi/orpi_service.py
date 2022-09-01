import logging
import requests

from ..target import Target

from .orpi_search_query import OrpiSearchQuery
from ..real_estate_service import RealEstateService
from ..real_estate import RealEstate
from ..settings import settings

class OrpiService(RealEstateService):
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.url = settings.orpi_url
    
    def search(self, query: OrpiSearchQuery) -> list[RealEstate]:
        response = requests.get(
            url=self.url,
            params=query.dict()
        )
        
        return RealEstate.from_response(response, Target.ORPI)