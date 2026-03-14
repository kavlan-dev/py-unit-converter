from fastapi import HTTPException

from py_unit_converter.schemas.conversion import ConversionRequest, ConversionResponse

UNIT_CONVERSION = {
    "length": {
        "millimeter": 1,
        "centimeter": 10,
        "meter": 1000,
        "kilometer": 1000000,
        "inch": 25.4,
        "foot": 304.8,
        "yard": 914.4,
        "mile": 1609344,
    },
    "weight": {
        "gram": 1,
        "kilogram": 1000,
        "pound": 453.592,
        "ounce": 28.3495,
    },
    "temperature": {
        "celsius": 1,
        "fahrenheit": 1.8,
        "kelvin": 1,
    },
}

UNIT_TYPES = {
    "millimeter": "length",
    "centimeter": "length",
    "meter": "length",
    "kilometer": "length",
    "inch": "length",
    "foot": "length",
    "yard": "length",
    "mile": "length",
    "gram": "weight",
    "kilogram": "weight",
    "pound": "weight",
    "ounce": "weight",
    "celsius": "temperature",
    "fahrenheit": "temperature",
    "kelvin": "temperature",
}


class ConvertService:
    def convert(self, request: ConversionRequest) -> ConversionResponse:
        from_unit_type = UNIT_TYPES.get(request.from_unit)
        to_unit_type = UNIT_TYPES.get(request.to_unit)

        if not from_unit_type or not to_unit_type:
            raise HTTPException(status_code=400, detail="Invalid unit")

        if from_unit_type != to_unit_type:
            raise HTTPException(
                status_code=400, detail="Cannot convert between different unit types"
            )

        if from_unit_type == "temperature":
            return self.convert_temperature(request)
        else:
            return self.convert_generic(request, from_unit_type)

    def convert_generic(
        self, request: ConversionRequest, unit_type: str
    ) -> ConversionResponse:
        from_value = UNIT_CONVERSION[unit_type].get(request.from_unit)
        to_value = UNIT_CONVERSION[unit_type].get(request.to_unit)

        if not from_value or not to_value:
            raise HTTPException(status_code=400, detail="Invalid unit")

        result = (request.value * from_value) / to_value
        return ConversionResponse(value=result)

    def convert_temperature(self, request: ConversionRequest) -> ConversionResponse:
        from_unit = request.from_unit
        to_unit = request.to_unit
        value = request.value

        if from_unit == "celsius":
            if to_unit == "fahrenheit":
                result = (value * 9 / 5) + 32
            elif to_unit == "kelvin":
                result = value + 273.15
            else:
                result = value
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                result = (value - 32) * 5 / 9
            elif to_unit == "kelvin":
                result = (value - 32) * 5 / 9 + 273.15
            else:
                result = value
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                result = value - 273.15
            elif to_unit == "fahrenheit":
                result = (value - 273.15) * 9 / 5 + 32
            else:
                result = value
        else:
            raise HTTPException(status_code=400, detail="Invalid unit")

        return ConversionResponse(value=result)
