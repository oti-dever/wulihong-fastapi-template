ARG PYTHON_VERSION=3.10.14
ARG PYPI_MIRROR_URL=https://pypi.org/simple

# build stage
FROM python:${PYTHON_VERSION}-bookworm AS builder
ARG PYPI_MIRROR_URL
WORKDIR /app

COPY . ./

RUN pip -V && \
    python -m pip install -i ${PYPI_MIRROR_URL} --upgrade pip && \
    pip config set global.index-url ${PYPI_MIRROR_URL} && \
    pip install Cython uv && \
    python setup.py build_ext -b lib && \
    mv uv.lock lib/ && \
    mv pyproject.toml lib/
RUN cd lib/ && uv sync --no-dev

# production stage
FROM python:${PYTHON_VERSION}-slim-bookworm
WORKDIR /app

COPY --from=builder /app/lib /app
COPY --from=builder /app/.env.production .env

ENV PATH=$PATH:/app/.venv/bin
EXPOSE 8000

CMD [ "/app/.venv/bin/python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
