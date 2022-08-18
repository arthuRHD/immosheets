import requests
from .seloger_search_query import SelogerSearchQuery
from ..real_estate import RealEstate
from ..real_estate_service import RealEstateService
from ..settings import settings
from ..target import Target

class SelogerService(RealEstateService):
    def __init__(self, api_key: str) -> None:
        self.url = settings.seloger_url
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": settings.seloger_host
        }
    
    def search(self, query: SelogerSearchQuery) -> list[RealEstate]:
        response = requests.get(
            self.url,
            headers=self.headers,
            params=query.dict()
        )

        total: int = response.json()['totalCount']        
        print(f"{total} real estates found.")
        
        return RealEstate.from_response(response, Target.SELOGER)
