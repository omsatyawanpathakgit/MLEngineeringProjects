In this project, I built a **text-completion model using an LSTM (Long Short-Term Memory) neural network** that is capable of learning the underlying patterns and word sequences present in poetry and generating meaningful text continuations based on the input provided by the end user.

For training the model, I collected **poems from various online sources** and used the collected poetry as a static dataset. I trained the LSTM model for **150 epochs** to learn the linguistic and structural patterns present in the dataset.

An LSTM model was chosen because it is well suited for **sequential data** and can retain relevant information from earlier parts of a sequence. This makes LSTM a suitable approach for text-generation and text-completion tasks, where the context of previously generated words plays an important role in predicting what should come next.

Before feeding the text data into the neural network, I performed several **text preprocessing steps**. These included converting the raw text into a suitable format, tokenizing the poems into sequences of tokens, and applying **padding** to sequences of different lengths so that all input sequences had the same length before being provided to the model for training.

During training, the model learns the underlying **linguistic and structural patterns** present in the poetry dataset. Given a sequence of words, the LSTM predicts the most probable next word. By repeatedly learning from these input-output sequences, the model gradually develops the ability to generate meaningful text continuations based on the context provided by the user.

## Run the sentence-completion website

The project includes a Flask backend and a simple HTML/CSS frontend. The backend loads `flower_poetry_lstm.pkl` and `tokenizer.pkl` from the project root and generates the requested number of next words.

1. Use Python 3.10–3.13 and install the backend dependencies:

   ```powershell
   python -m pip install -r backend/requirements.txt
   ```

2. The backend reads its settings from `backend/.env`.

3. From the project root, start the Flask server:

   ```powershell
   python backend/app.py
   ```

4. Open <http://127.0.0.1:5000> in your browser, enter a sentence, and choose how many words to generate (up to 30).

The saved model is a Python pickle and depends on compatible TensorFlow/Keras versions. Keep the model and tokenizer files in the project root; the server loads them the first time a completion is requested. Install the requirements into the same Python environment used to run Flask, then restart the server.
