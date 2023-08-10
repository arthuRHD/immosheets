import requests
from deprecated import deprecated
from ..target import Target
from ..real_estate import RealEstate
from .leboncoin_search_query import LeboncoinSearchQuery
from ..real_estate_service import RealEstateService
from ..settings import settings


class LeboncoinService(RealEstateService):
    @deprecated(version='1.1.1', reason="leboncoin is now using datadome which bans bots.")
    def __init__(self, api_key: str) -> None:
        self.url = settings.leboncoin_url
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": settings.leboncoin_host
        }

    @deprecated(version='1.1.1', reason="leboncoin is now using datadome which bans bots.")
    def search(self, query: LeboncoinSearchQuery) -> list[RealEstate]:
        response = requests.post(
            self.url,
            headers=self.headers,
            timeout=settings.request_timeout_in_secs,
            data=query.model_dump()
        )

        return RealEstate.from_response(response, Target.LEBONCOIN)
