
FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    gcc

WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt


COPY . /app


EXPOSE 8000


CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
