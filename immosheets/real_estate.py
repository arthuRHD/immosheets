from pydantic import BaseModel
from requests import Response
from .target import Target

class RealEstate(BaseModel):
    price: int
    bedrooms: int
    rooms: int
    city: str
    space: float
    link: str
    pro_name: str | None
    pro_email: str | None
    pro_tel: str | None
    
    def to_cell(self) -> list:
        """Prepare the data in a cell format in order to facilitate the insertion.

        :return: A list of each attributes
        :rtype: list
        """
        return [self.price, self.bedrooms, self.rooms, self.city, self.space, self.link, self.pro_name, self.pro_email, self.pro_tel]

    @staticmethod
    def from_response(response: Response, target: Target):
        match target:
            case Target.SELOGER:
                return [ 
                    RealEstate(
                    price=raw['price'], 
                    bedrooms=raw['bedrooms'], 
                    rooms=raw['rooms'], 
                    space=raw['livingArea'],
                    city=raw['city'], 
                    link=raw['permalink'], 
                    pro_email=raw['professional']['email'], 
                    pro_name=raw['professional']['name'], 
                    pro_tel=raw['professional']['phoneNumber']
                ) for raw in response.json()['items'] 
                ]
            case Target.LEBONCOIN:
                raise NotImplementedError
            case _:
                raise NotImplementedError