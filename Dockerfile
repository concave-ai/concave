FROM python:3.11-alpine3.19



RUN apk add supervisor
WORKDIR /app
RUN pip install poetry
ADD pyproject.toml poetry.lock /app/
RUN poetry install --no-root
COPY . /app
CMD ["supervisord", "-c", "/app/scripts/supervisord.conf"]