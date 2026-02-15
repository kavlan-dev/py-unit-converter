from fastapi.middleware.cors import CORSMiddleware

from py_unit_converter.main import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
