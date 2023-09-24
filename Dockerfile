FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn src.infra.fastapi:app --host 0.0.0.0 --port 80 --reload