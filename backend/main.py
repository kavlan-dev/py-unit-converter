from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Модель для запроса
class ConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str


# Коэффициенты конвертации для длины
LENGTH_CONVERSION = {
    "millimeter": 1,
    "centimeter": 10,
    "meter": 1000,
    "kilometer": 1000000,
    "inch": 25.4,
    "foot": 304.8,
    "yard": 914.4,
    "mile": 1609344,
}

# Коэффициенты конвертации для массы
WEIGHT_CONVERSION = {
    "gram": 1,
    "kilogram": 1000,
    "pound": 453.592,
    "ounce": 28.3495,
}

# Коэффициенты конвертации для температуры
TEMPERATURE_CONVERSION = {
    "celsius": 1,
    "fahrenheit": 1.8,
    "kelvin": 1,
}


@app.post("/api/convert/length")
def convert_length(request: ConversionRequest):
    from_value = LENGTH_CONVERSION.get(request.from_unit)
    to_value = LENGTH_CONVERSION.get(request.to_unit)

    if from_value is None or to_value is None:
        raise HTTPException(status_code=400, detail="Invalid unit")

    result = (request.value * from_value) / to_value
    return {
        "result": result,
        "from_unit": request.from_unit,
        "to_unit": request.to_unit,
    }


@app.post("/api/convert/temperature")
def convert_temperature(request: ConversionRequest):
    from_value = TEMPERATURE_CONVERSION.get(request.from_unit)
    to_value = TEMPERATURE_CONVERSION.get(request.to_unit)

    if from_value is None or to_value is None:
        raise HTTPException(status_code=400, detail="Invalid unit")

    result = (request.value * from_value) / to_value
    return {
        "result": result,
        "from_unit": request.from_unit,
        "to_unit": request.to_unit,
    }


@app.post("/api/convert/weight")
def convert_weight(request: ConversionRequest):
    from_value = WEIGHT_CONVERSION.get(request.from_unit)
    to_value = WEIGHT_CONVERSION.get(request.to_unit)

    if from_value is None or to_value is None:
        raise HTTPException(status_code=400, detail="Invalid unit")

    result = (request.value * from_value) / to_value
    return {
        "result": result,
        "from_unit": request.from_unit,
        "to_unit": request.to_unit,
    }
