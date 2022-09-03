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
        url: str = self.url + query.parse_transaction_type() + query.parse_real_estate_types() + query.parse_locations()
        response = requests.get(
            url=requests.utils.unquote(url.rstrip(url[-1])),
            params=query.dict(exclude={'realEstateTypes', 'locations', 'transactionType'})
        )
        
        if response.status_code == 200:
            self.logger.info(f"we found {len(response.json()['items'])} real estates.")
        else:
            self.logger.error(f"something went wrong: HTTP {response.status_code}")
        
        return RealEstate.from_response(response, Target.ORPI)