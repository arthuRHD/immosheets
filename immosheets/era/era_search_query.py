from pydantic import field_validator, BaseModel, Field, ConfigDict


class PostalCode(BaseModel):
    value: str | None = None

    @field_validator('value')
    @classmethod
    def postal_code_is_correct(cls, value: str | None):
        separator: str = ","

        if value is None:
            raise ValueError("zipcode is not set")
        if value == "":
            raise ValueError(f"{value} must have at least one zipcode")

        if separator in value:
            for code in value.split(separator):
                if not code.isdigit():
                    raise ValueError(f"{code} are not digits")
        else:
            if not value.isdigit():
                raise ValueError(f"{code} are not digits")

        return value


class EraTransactionType:
    RENT: str = "louer"
    BUY: str = "acheter"


class EraRealEstateType:
    HOUSE: str = "maison"
    APPARTMENT: str = "appartement"
    DUPLEX: str = "duplex"
    LAND: str = "terrain"
    OFFICE: str = "bureaux"
    COMMERCIAL: str = "local commercial,fonds de commerce,entrepôts"


class EraSearchQuery(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    page_size: int = Field(alias="per_page", default=1000)
    distance: int = 0
    real_estate_type: list[str] | None = Field(None, alias="type_bien")
    transaction_type: str = Field(alias="annonce_type")
    transaction_type_bis: str | None = Field(None, alias="type_annonce")
    location_id: str | None = Field(None, alias="geo_ville_id")
    min_square_meter: int = Field(alias="surface_from", default=1)
    max_square_meter: int = Field(alias="surface_to", default=500)
    min_price: int = Field(alias="prix_from", default=10)
    max_price: int | None = Field(None, alias="prix_to")
    rooms: int = Field(alias="nb_pieces", default=1)
    bedrooms: int = Field(alias="nb_chambres", default=1)
    fields: str = "id"
    page: int = 1
    sort_by: str = "desc"
    reused: bool = Field(alias="shouldReuse", default=True)
    format: str = Field(alias="_format", default="json")
