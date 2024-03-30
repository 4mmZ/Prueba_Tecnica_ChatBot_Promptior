FROM python:3.12.2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "uvicorn app.server:app --host 0.0.0.0 --port $PORT"]
CMD uvicorn app.server:app --host 0.0.0.0 --reload --port $PORT

EXPOSE $PORT
