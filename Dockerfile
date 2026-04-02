# syntax=docker/dockerfile:1

FROM node:22-slim AS frontend

# TODO move this into the python builder stage, use uv-managed node

WORKDIR /build
COPY mex/editor/client/ .
RUN npm ci
RUN npx ng build --output-path /dist/root
RUN npx ng build --base-href /editor/ --output-path /dist/subpath

FROM python:3.14 AS builder

WORKDIR /build

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_NO_INPUT=on
ENV PIP_PREFER_BINARY=on
ENV PIP_PROGRESS_BAR=off

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN uv export --no-dev --no-hashes --output-file requirements.lock

RUN pip wheel --no-cache-dir --wheel-dir /build/wheels -r requirements.lock
RUN pip wheel --no-cache-dir --wheel-dir /build/wheels --no-deps .

FROM python:3.14-slim

LABEL org.opencontainers.image.authors="mex@rki.de"
LABEL org.opencontainers.image.description="The editor enables anyone to create and edit entities in a simple and fast way."
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.url="https://github.com/robert-koch-institut/mex-editor-ng"
LABEL org.opencontainers.image.vendor="robert-koch-institut"

ENV PYTHONUNBUFFERED=1
ENV PYTHONOPTIMIZE=1

WORKDIR /app

COPY --from=builder /build/wheels /wheels

RUN pip install --no-cache-dir \
    --no-index \
    --find-links=/wheels \
    /wheels/*.whl \
    && rm -rf /wheels

RUN adduser \
    --disabled-password \
    --gecos "" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "10001" \
    mex

COPY --from=frontend --chown=mex /dist/root /app/dist/root
COPY --from=frontend --chown=mex /dist/subpath /app/dist/subpath

USER mex

EXPOSE 8000

ENTRYPOINT [ "editor", "--static-dir", "/app/dist/root" ]
