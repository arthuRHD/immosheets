from typing import List

import requests
from .seloger_search_query import SelogerSearchQuery
from .real_estate import RealEstate
from .real_estate_service import RealEstateService
from .settings import settings


class SelogerService(RealEstateService):
    def __init__(self, api_key: str) -> None:
        self.url = settings.seloger_url
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": settings.rapidapi_host
        }
    
    def search(self, query: SelogerSearchQuery) -> List[RealEstate]:
        response = requests.get(
            self.url,
            headers=self.headers,
            params=query.dict()
        )
            
        results = [
            RealEstate(
                price=item['price'], 
                bedrooms=item['bedrooms'], 
                rooms=item['rooms'], 
                space=item['livingArea'],
                city=item['city'], 
                link=item['permalink'], 
                pro_email=item['professional']['email'], 
                pro_name=item['professional']['name'], 
                pro_tel=item['professional']['phoneNumber']
            ) for item in response.json()['items']
        ]
        
        print(f"{response.json()['totalCount']} real estates found.")
        
        return results
