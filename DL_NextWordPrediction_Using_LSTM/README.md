In this project, I built a **text-completion model using an LSTM (Long Short-Term Memory) neural network** that is capable of learning the underlying patterns and word sequences present in poetry and generating meaningful text continuations based on the input provided by the end user.

For training the model, I collected **poems from various online sources** and used the collected poetry as a static dataset. I trained the LSTM model for **150 epochs** to learn the linguistic and structural patterns present in the dataset.

An LSTM model was chosen because it is well suited for **sequential data** and can retain relevant information from earlier parts of a sequence. This makes LSTM a suitable approach for text-generation and text-completion tasks, where the context of previously generated words plays an important role in predicting what should come next.

Before feeding the text data into the neural network, I performed several **text preprocessing steps**. These included converting the raw text into a suitable format, tokenizing the poems into sequences of tokens, and applying **padding** to sequences of different lengths so that all input sequences had the same length before being provided to the model for training.

During training, the model learns the underlying **linguistic and structural patterns** present in the poetry dataset. Given a sequence of words, the LSTM predicts the most probable next word. By repeatedly learning from these input-output sequences, the model gradually develops the ability to generate meaningful text continuations based on the context provided by the user.

## Run the sentence-completion website

The project includes a Flask backend and a simple HTML/CSS frontend. The backend loads `flower_poetry_lstm.pkl` and `tokenizer.pkl` from the project root and generates the requested number of next words.

1. Create a project-specific virtual environment in a short per-user path. This avoids Windows long-path failures when installing TensorFlow:

   ```powershell
   $venv = Join-Path $env:USERPROFILE ".venvs\dl-nextwordprediction"
   py -3.13 -m venv $venv
   & "$venv\Scripts\python.exe" -m pip install --upgrade pip
   & "$venv\Scripts\python.exe" -m pip install -r requirements.txt
   ```

2. The backend reads local settings from `backend/.env`. Keep the virtual environment and `.env` local; do not commit them.

3. From the project root, start the Flask server using that environment:

   ```powershell
   & "$venv\Scripts\python.exe" backend\app.py
   ```

   The development server disables automatic reloading because loading the TensorFlow model can otherwise trigger file-watcher restarts and interrupt requests.

4. Open <http://127.0.0.1:5000> in your browser, enter a sentence, and choose how many words to generate (up to 40).

The saved model is a Python pickle and depends on compatible TensorFlow/Keras versions. Keep the model and tokenizer files in the project root; the server loads them the first time a completion is requested. The local virtual environment is not copied into Docker; Docker installs the same dependencies from `requirements.txt`.

## Run with Docker

Build and run the container from the project root:

```powershell
docker build -t flower-poetry-generator .
docker run --rm -p 8000:8000 flower-poetry-generator
```

Open <http://127.0.0.1:8000>. The image installs the dependencies from `requirements.txt`; it does not copy the Windows `.venv` or `backend/.env`.

## Publish Docker images with GitHub Actions

The workflow at `../.github/workflows/dl-nextwordprediction-docker.yml` builds and pushes an image after pushes that change this project. GitHub requires active workflow files to be stored in the repository-root `.github/workflows` directory, so a workflow inside this project folder would not run. Each project push publishes branch and commit-SHA tags; pushes to the default branch also update `latest`. To enable it:

1. Create a Docker Hub repository named `flower-poetry-generator`.
2. In Docker Hub, create an access token with permission to push images.
3. In the GitHub repository, open **Settings → Secrets and variables → Actions → New repository secret** and add:
   - `DOCKERHUB_USERNAME`: your Docker Hub username.
   - `DOCKERHUB_TOKEN`: the Docker Hub access token (not your password).
4. Commit and push the project and workflow files. In the repository's **Actions** tab, open **Build and push poetry predictor image** to follow the build.

The workflow publishes a branch tag, a commit-SHA tag, and `latest` for the default branch. The resulting image is `DOCKERHUB_USERNAME/flower-poetry-generator`.
