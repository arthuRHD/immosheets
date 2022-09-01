import requests
from typing import Generator
import logging
from .seloger_search_query import SelogerSearchQuery
from ..real_estate import RealEstate
from ..real_estate_service import RealEstateService
from ..settings import settings
from ..target import Target

class SelogerService(RealEstateService):
    def __init__(self, api_key: str) -> None:
        self.logger = logging.getLogger(__name__)
        self.url = settings.seloger_url
        self.session = requests.Session()
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": settings.seloger_host
        }
    
    def search(self, query: SelogerSearchQuery) -> Generator[list[RealEstate], None, None]:
        retrieve_page = lambda q: self.session.get(
            url=self.url,
            headers=self.headers,
            params=q.dict()
        )

        total: int = retrieve_page(query).json()['totalCount']     
        num_pages: int = total // int(settings.page_size)
        self.logger.info(f"we found {num_pages} pages")

        for page in range(2, num_pages + 1):
            self.logger.info(f"page: {query.pageIndex}")
            query.pageIndex = page

            yield RealEstate.from_response(retrieve_page(query), Target.SELOGER)
