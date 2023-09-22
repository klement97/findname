FROM python:3.11-slim

WORKDIR /src

COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY src/ .
CMD uvicorn infra.fastapi:app --host 0.0.0.0 --port 80 --reload