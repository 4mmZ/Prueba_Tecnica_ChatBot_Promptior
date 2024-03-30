FROM python:3.12.2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD uvicorn app.server:app --host 0.0.0.0 --port $PORT

EXPOSE 8000
