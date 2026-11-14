import os
import pickle
import threading
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory


BACKEND_DIR = Path(__file__).resolve().parent
load_dotenv(BACKEND_DIR / ".env")

PROJECT_DIR = (BACKEND_DIR / os.environ["PROJECT_DIR"]).resolve()
FRONTEND_DIR = PROJECT_DIR / os.environ["FRONTEND_DIR"]
MODEL_PATH = PROJECT_DIR / os.environ["MODEL_PATH"]
TOKENIZER_PATH = PROJECT_DIR / os.environ["TOKENIZER_PATH"]
MAX_SEQUENCE_LENGTH = int(os.environ["MAX_SEQUENCE_LENGTH"])
MAX_WORDS_TO_GENERATE = int(os.environ["MAX_WORDS_TO_GENERATE"])

app = Flask(
    __name__,
    static_folder=str(FRONTEND_DIR),
    static_url_path="/static",
)

_model = None
_tokenizer = None
_resource_lock = threading.Lock()


def load_resources():
    global _model, _tokenizer

    if _model is None or _tokenizer is None:
        with _resource_lock:
            if _model is None or _tokenizer is None:
                with MODEL_PATH.open("rb") as model_file:
                    model = pickle.load(model_file)
                with TOKENIZER_PATH.open("rb") as tokenizer_file:
                    tokenizer = pickle.load(tokenizer_file)
                _model = model
                _tokenizer = tokenizer

    return _model, _tokenizer


def generate_completion(text, words_to_generate, model, tokenizer):
    completion = text
    token_to_word = {
        index: word for word, index in tokenizer.word_index.items()
    }

    for _ in range(words_to_generate):
        token_sequence = tokenizer.texts_to_sequences([completion])[0]
        token_sequence = token_sequence[-MAX_SEQUENCE_LENGTH:]
        padded_sequence = np.zeros((1, MAX_SEQUENCE_LENGTH), dtype=np.int32)
        if token_sequence:
            padded_sequence[0, -len(token_sequence):] = token_sequence

        probabilities = model.predict(padded_sequence, verbose=0)
        next_word = token_to_word.get(int(np.argmax(probabilities, axis=-1)[0]))
        if next_word is None:
            break
        completion = f"{completion} {next_word}"

    return completion


@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.post("/api/complete")
def complete():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="Send a JSON object with a text field."), 400

    text = data.get("text")
    if not isinstance(text, str) or not text.strip():
        return jsonify(error="Enter a sentence to complete."), 400

    words = data.get("words", 10)
    if type(words) is not int or not 1 <= words <= MAX_WORDS_TO_GENERATE:
        return jsonify(
            error=f"Words must be an integer between 1 and {MAX_WORDS_TO_GENERATE}."
        ), 400

    try:
        model, tokenizer = load_resources()
    except ModuleNotFoundError as error:
        return jsonify(
            error=(
                f"Missing Python package '{error.name}'. Install backend/requirements.txt "
                "in the same Python environment running Flask, then restart the server."
            )
        ), 503
    except (ImportError, OSError, pickle.UnpicklingError, AttributeError) as error:
        return jsonify(
            error=f"Could not load the model or tokenizer: {error}"
        ), 503

    completion = generate_completion(text.strip(), words, model, tokenizer)
    return jsonify(completion=completion)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
