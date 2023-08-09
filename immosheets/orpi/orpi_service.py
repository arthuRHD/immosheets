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
        url: str = self.url + query.parse_transaction_type() + \
            query.parse_real_estate_types() + query.parse_locations()
        response = requests.get(
            url=requests.utils.unquote(url.rstrip(url[-1])),
            timeout=settings.request_timeout_in_secs,
            params=query.model_dump(
                exclude={'realEstateTypes', 'locations', 'transactionType'})
        )

        if response.status_code == 200:
            self.logger.info("we found %s real estates.",
                             len(response.json()['items']))
        else:
            self.logger.error("something went wrong: HTTP %s",
                              response.status_code)

        return RealEstate.from_response(response, Target.ORPI)
