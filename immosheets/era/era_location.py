from pydantic import BaseModel, Field, ConfigDict


class Town(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    type: str
    name: str = Field(alias="nom")
    postal_code: str = Field(alias="code_postal")
    slug: str
    code: str


class Department(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str = Field(alias="nom")
    slug: str
    code: str


class EraLocationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    departments: list[Department] | None = Field(None, alias="departements")
    towns: list[Town] | None = Field(None, alias="villes")


class EraLocationRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    postal_code: str = Field(alias="query")
    format: str = Field(alias="_format", default="json")
