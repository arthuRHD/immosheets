import attr
from typing import Optional

@attr.s(auto_attribs=True)
class Range:
    min: Optional[int] = None
    max: Optional[int] = None
