FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY flower_poetry_lstm.pkl tokenizer.pkl ./

ENV PROJECT_DIR=.. \
    FRONTEND_DIR=frontend \
    MODEL_PATH=flower_poetry_lstm.pkl \
    TOKENIZER_PATH=tokenizer.pkl \
    MAX_SEQUENCE_LENGTH=56 \
    MAX_WORDS_TO_GENERATE=40 \
    PORT=8000

EXPOSE 8000

CMD ["sh", "-c", "waitress-serve --listen=0.0.0.0:${PORT:-8000} backend.app:app"]
