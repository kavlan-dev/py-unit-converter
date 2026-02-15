from fastapi import HTTPException

from py_unit_converter.schemas.conversion import Conversion
from py_unit_converter.utils.util import (
    LENGTH_CONVERSION,
    TEMPERATURE_CONVERSION,
    WEIGHT_CONVERSION,
)


class Service:
    def convert_length(self, value: float, from_unit: str, to_unit: str) -> Conversion:
        from_value = LENGTH_CONVERSION.get(from_unit)
        to_value = LENGTH_CONVERSION.get(to_unit)

        if not from_value or not to_value:
            raise HTTPException(status_code=400, detail="Invalid unit")

        result = (value * from_value) / to_value
        return Conversion(
            value=result,
            from_unit=from_unit,
            to_unit=to_unit,
        )

    def convert_weight(self, value: float, from_unit: str, to_unit: str) -> Conversion:
        from_value = WEIGHT_CONVERSION.get(from_unit)
        to_value = WEIGHT_CONVERSION.get(to_unit)

        if from_value is None or to_value is None:
            raise HTTPException(status_code=400, detail="Invalid unit")

        result = (value * from_value) / to_value
        return Conversion(
            value=result,
            from_unit=from_unit,
            to_unit=to_unit,
        )

    def convert_temperature(
        self, value: float, from_unit: str, to_unit: str
    ) -> Conversion:
        from_value = TEMPERATURE_CONVERSION.get(from_unit)
        to_value = TEMPERATURE_CONVERSION.get(to_unit)

        if from_value is None or to_value is None:
            raise HTTPException(status_code=400, detail="Invalid unit")

        result = (value * from_value) / to_value
        return Conversion(
            value=result,
            from_unit=from_unit,
            to_unit=to_unit,
        )
