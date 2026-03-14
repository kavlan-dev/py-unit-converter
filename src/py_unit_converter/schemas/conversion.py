from pydantic import BaseModel


class ConversionBase(BaseModel):
    pass


class ConversionResponse(ConversionBase):
    value: float


class ConversionRequest(ConversionBase):
    value: float
    from_unit: str
    to_unit: str
