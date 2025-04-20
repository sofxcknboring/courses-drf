FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev libjpeg-dev zlib1g-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn config:wsgi:application --bind 0.0.0.0:8000"]