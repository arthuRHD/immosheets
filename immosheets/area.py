import attr


@attr.s(auto_attribs=True)
class Area:
    lat: float
    lng: float
    default_radius: int = 5000
    radius: int
