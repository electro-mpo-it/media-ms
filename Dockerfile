FROM python:3.11-slim

WORKDIR /app

COPY ./ /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD uvicorn main:app --port=8000