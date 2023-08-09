from pydantic import field_validator, BaseModel


class PostalCode(BaseModel):
    value: str | None = None

    @field_validator('value')
    @classmethod
    def postal_code_is_correct(cls, value: str | None):
        separator: str = ","

        assert value != "", "must have at least one zipcode"

        if separator in value:
            for code in value.split(separator):
                assert code.isdigit(), f"{code} are not digits"
        else:
            assert value.isdigit(), f"{value} are not digits"

        return value
