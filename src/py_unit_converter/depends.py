from py_unit_converter.services.service import ConvertService

convert_service = ConvertService()


def get_convert_service() -> ConvertService:
    return convert_service
