FROM python:3.10.0-alpine as base

# Prevent stdout/stderr buffering
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
        python3-dev \
        gcc \
        g++ \
        musl-dev \
        libffi-dev \
        libressl-dev \
        libxml2-dev \
        libxslt-dev \
        make \
        bash \
 && pip install --no-cache-dir poetry

# layer for changing modules (should not change frequently)
WORKDIR /code

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction

# src layer (changes frequently)
COPY . .

RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction

EXPOSE 9080/tcp

# reset pristine db every run
ENTRYPOINT cp /code/database/pristine/* /code/database && example_api --reload --config-file sample_config.toml
