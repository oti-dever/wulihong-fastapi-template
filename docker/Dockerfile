ARG PYTHON_VERSION=3.10.14
ARG PYPI_MIRROR_URL=https://pypi.org/simple

# build stage
FROM python:${PYTHON_VERSION}-bookworm as builder
ARG PYPI_MIRROR_URL
WORKDIR /app

COPY . ./

RUN pip -V && \
    python -m pip install -i ${PYPI_MIRROR_URL} --upgrade pip && \
    pip config set global.index-url ${PYPI_MIRROR_URL} && \
    pip install Cython && \
    python setup.py build_ext -b lib && \
    mv poetry.lock lib/ && \
    mv pyproject.toml lib/

# production stage
FROM python:${PYTHON_VERSION}-slim-bookworm
ARG PYPI_MIRROR_URL
WORKDIR /app

COPY --from=builder /app/lib /app

RUN pip -V && \
    python -m pip install -i ${PYPI_MIRROR_URL} --upgrade pip && \
    pip config set global.index-url ${PYPI_MIRROR_URL} && \
    pip install poetry

RUN python -m venv venv && \
    . venv/bin/activate && \
    poetry install --only main --no-interaction --no-ansi

ENV PATH=$PATH:/app/venv/bin
EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
