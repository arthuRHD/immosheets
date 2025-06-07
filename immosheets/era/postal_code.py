import attr
from typing import Optional


def _validate_postal_code(instance, attribute, value: Optional[str]):
    """
    Validates if the postal code(s) are correctly formatted digits,
    handling single codes or comma-separated lists.
    """
    separator: str = ","

    if value == "" or value is None:
        raise ValueError("must have at least one zipcode")

    if separator in value:
        for code in value.split(separator):
            if not code.isdigit():
                raise ValueError(f"'{code}' are not digits")
    else:
        if not value.isdigit():
            raise ValueError(f"'{value}' are not digits")


@attr.s(auto_attribs=True, frozen=True)
class PostalCode:
    value: Optional[str] = attr.field(validator=_validate_postal_code)
