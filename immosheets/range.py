from pydantic import BaseModel

class Range(BaseModel):
    min: int | None = None
    max: int | None = None