from ..target import Target
from ..real_estate import RealEstate
from .leboncoin_search_query import LeboncoinSearchQuery
from ..real_estate_service import RealEstateService
from ..settings import settings
import requests

class LeboncoinService(RealEstateService):
    def __init__(self, api_key: str) -> None:
        self.url = settings.leboncoin_url
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": settings.leboncoin_host
        }
        raise DeprecationWarning(message="leboncoin is now using datadome which bans bots.")

    def search(self, query: LeboncoinSearchQuery) -> list[RealEstate]:
        response = requests.post(
            self.url,
            headers=self.headers,
            data=query.dict()
        )

        return RealEstate.from_response(response, Target.LEBONCOIN)
