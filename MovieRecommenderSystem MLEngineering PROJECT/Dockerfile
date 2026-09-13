FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend

COPY movies.pkl .
COPY similarity.pkl .
COPY movies_recommender_system.pkl .

EXPOSE 5000

CMD ["python", "backend/app.py"]