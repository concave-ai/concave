poetry run python3 apps/verify.py
poetry run gunicorn apps.api:app --worker-class uvicorn.workers.UvicornWorker --workers 2 --bind 0.0.0.0:6080