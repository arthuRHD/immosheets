from pydantic import BaseModel

class Range(BaseModel):
    min: int | None
    max: int | None