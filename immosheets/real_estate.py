import attr
from requests import Response
from .target import Target


@attr.s(auto_attribs=True)
class RealEstate:
    price: int
    bedrooms: Optional[int] = None
    rooms: int
    city: str
    space: float
    link: Optional[str] = None
    pro_name: Optional[str] = None
    pro_email: Optional[str] = None
    pro_tel: Optional[str] = None
    provider: str

    def to_cell(self) -> list:
        """Prepare the data in a cell format in order to facilitate the insertion.

        :return: A list of each attributes
        :rtype: list
        """
        return [self.price, self.bedrooms, self.rooms, self.city, self.space, self.link,
                self.pro_name, self.pro_email, self.pro_tel, self.provider]

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
                        pro_tel=raw['professional']['phoneNumber'],
                        provider='SELOGER'
                    ) for raw in response.json()['items']
                ]
            case Target.ORPI:
                base_url: str = "https://www.orpi.com/annonce"
                return [
                    RealEstate(
                        price=raw['price'],
                        bedrooms=raw['nbBedrooms'],
                        rooms=raw['nbRooms'],
                        space=raw['surface'],
                        city=raw['city']['name'],
                        link=f"{base_url}-{'location' if raw['transaction'] == 'rent' else 'aa'}-{raw['slug']}",
                        pro_email=raw['agency']['email'],
                        pro_name=raw['agency']['name'],
                        pro_tel=raw['agency']['phone'],
                        provider='ORPI'
                    ) for raw in response.json()['items'] if not raw['sold']
                ]
            case Target.LEBONCOIN:
                raise NotImplementedError
            case _:
                raise NotImplementedError
