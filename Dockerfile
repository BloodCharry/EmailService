FROM python:2.7-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

#RUN useradd --create-home celery

WORKDIR /app

ENV PYTHONPATH=/app/email_service

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN chown -R celery:celery /app
#USER celery

CMD ["python", "email_service/manage.py", "runserver", "0.0.0.0:8000"]