from fastapi import APIRouter, Depends

from py_unit_converter.schemas.conversion import Conversion
from py_unit_converter.services.service import Service

router = APIRouter(prefix="/api/convert", tags=["Conversion"])


def get_service():
    return Service()


@router.post("/length", response_model=Conversion)
def convert_length(
    request: Conversion, service: Service = Depends(get_service)
) -> Conversion:
    return service.convert_length(request.value, request.from_unit, request.to_unit)


@router.post("/temperature", response_model=Conversion)
def convert_temperature(
    request: Conversion, service: Service = Depends(get_service)
) -> Conversion:
    return service.convert_temperature(
        request.value, request.from_unit, request.to_unit
    )


@router.post("/weight", response_model=Conversion)
def convert_weight(
    request: Conversion, service: Service = Depends(get_service)
) -> Conversion:
    return service.convert_weight(request.value, request.from_unit, request.to_unit)
