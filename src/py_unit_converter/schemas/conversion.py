from pydantic import BaseModel


class Conversion(BaseModel):
    value: float
    from_unit: str
    to_unit: str
