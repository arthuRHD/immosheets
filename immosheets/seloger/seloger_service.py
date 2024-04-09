import logging
from typing import Generator
import requests
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

    def retrieve_page(self, query: SelogerSearchQuery) -> requests.Response:
        return self.session.get(
            url=self.url,
            headers=self.headers,
            timeout=settings.request_timeout_in_secs,
            params=query.model_dump()
        )

    def search(self, query: SelogerSearchQuery) -> Generator[list[RealEstate], None, None]:
        total: int = self.retrieve_page(query).json()['totalCount']
        num_pages: int = total // int(settings.page_size)
        self.logger.info("we found %s pages", num_pages)

        for page in range(2, num_pages + 1):
            self.logger.info("page: %s", query.pageIndex)
            query.pageIndex = page

            yield RealEstate.from_response(self.retrieve_page(query), Target.SELOGER)
