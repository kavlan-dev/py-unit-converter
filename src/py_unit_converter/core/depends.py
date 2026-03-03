from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from py_unit_converter.routers.router import get_router


def get_app() -> FastAPI:
    router = get_router()

    app = FastAPI()
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
