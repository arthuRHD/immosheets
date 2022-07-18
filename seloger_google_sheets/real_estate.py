from typing import Optional
from pydantic import BaseModel

class RealEstate(BaseModel):
    price: int
    bedrooms: int
    rooms: int
    city: str
    space: float
    link: str
    pro_name: Optional[str]
    pro_email: Optional[str]
    pro_tel: Optional[str]
    
    def to_cell(self) -> list:
        """Prepare the data in a cell format in order to facilitate the insertion.

        :return: A list of each attributes
        :rtype: list
        """
        return [self.price, self.bedrooms, self.rooms, self.city, self.space, self.link, self.pro_name, self.pro_email, self.pro_tel]
