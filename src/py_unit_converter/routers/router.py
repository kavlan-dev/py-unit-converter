from fastapi import APIRouter, Depends, status

from py_unit_converter.core.depends import get_convert_service
from py_unit_converter.schemas.conversion import Conversion
from py_unit_converter.services.service import ConvertService

router = APIRouter(prefix="/api/convert", tags=["Conversion"])


def get_router() -> APIRouter:
    return router


@router.post("/length", response_model=Conversion, status_code=status.HTTP_200_OK)
def convert_length(
    request: Conversion, service: ConvertService = Depends(get_convert_service)
) -> Conversion:
    return service.convert_length(request.value, request.from_unit, request.to_unit)


@router.post("/temperature", response_model=Conversion, status_code=status.HTTP_200_OK)
def convert_temperature(
    request: Conversion, service: ConvertService = Depends(get_convert_service)
) -> Conversion:
    return service.convert_temperature(
        request.value, request.from_unit, request.to_unit
    )


@router.post("/weight", response_model=Conversion, status_code=status.HTTP_200_OK)
def convert_weight(
    request: Conversion, service: ConvertService = Depends(get_convert_service)
) -> Conversion:
    return service.convert_weight(request.value, request.from_unit, request.to_unit)
