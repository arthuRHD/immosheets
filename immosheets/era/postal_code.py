from pydantic import field_validator, BaseModel


class PostalCode(BaseModel):
    value: str | None = None

    @field_validator('value')
    @classmethod
    def postal_code_is_correct(cls, value: str | None):
        separator: str = ","

        if value == "":
            raise ValueError("must have at least one zipcode")

        if separator in value:
            for code in value.split(separator):
                if not code.isdigit():
                    raise ValueError(f"{code} are not digits")
        else:
            if not value.isdigit():
                raise ValueError(f"{value} are not digits")

        return value
