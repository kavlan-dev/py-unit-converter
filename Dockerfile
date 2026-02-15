FROM python:3.13-slim
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

COPY poetry.lock pyproject.toml ./
COPY README.md ./
COPY src/ src/

RUN poetry install

CMD ["poetry", "run", "python", "src/py_unit_converter/main.py"]
