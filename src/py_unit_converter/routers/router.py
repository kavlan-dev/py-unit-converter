from fastapi import APIRouter, Depends, status

from py_unit_converter.schemas.conversion import ConversionRequest, ConversionResponse
from src.py_unit_converter.depends import get_convert_service
from src.py_unit_converter.services.service import ConvertService

router = APIRouter(prefix="/api/convert", tags=["Conversion"])


def get_router() -> APIRouter:
    return router


@router.post(
    "/length", response_model=ConversionResponse, status_code=status.HTTP_200_OK
)
def convert_length(
    request: ConversionRequest, service: ConvertService = Depends(get_convert_service)
) -> ConversionResponse:
    return service.convert(request)


@router.post(
    "/temperature", response_model=ConversionResponse, status_code=status.HTTP_200_OK
)
def convert_temperature(
    request: ConversionRequest, service: ConvertService = Depends(get_convert_service)
) -> ConversionResponse:
    return service.convert(request)


@router.post(
    "/weight", response_model=ConversionResponse, status_code=status.HTTP_200_OK
)
def convert_weight(
    request: ConversionRequest, service: ConvertService = Depends(get_convert_service)
) -> ConversionResponse:
    return service.convert(request)
