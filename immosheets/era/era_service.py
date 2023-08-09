import logging
from requests import Session
from ..settings import settings
from .postal_code import PostalCode
from .era_search_query import EraSearchQuery
from ..real_estate import RealEstate
from ..real_estate_service import RealEstateService
from .era_location import EraLocationResponse, EraLocationRequest


class EraService(RealEstateService):
    def __init__(self, session: Session) -> None:
        self.logger = logging.getLogger(__name__)
        self.url = settings.era_url
        self.session = session

    def fill_with_town_id(self, query: EraSearchQuery, postal_code: PostalCode) -> EraSearchQuery:
        request = EraLocationRequest(postal_code=postal_code)
        response: EraLocationResponse = self.session.get(
            f"{self.url}/ville-departement", params=request.model_dump(by_alias=True)).json()
        query.location_id = response.towns[0].id
        return query

    def search(self, query: EraSearchQuery) -> list[RealEstate]:
        ...
