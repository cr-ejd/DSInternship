# QA Service 🤖📚
*A Question Answering (QA) service using a Hugging Face model with FastAPI*

## 🚀 Overview
This project is a **FastAPI**-based **Question Answering (QA) service** utilizing a **Hugging Face model** to extract answers from given text.

## 💂️ Project Structure
```
📺 DSInternship
 ┓ 📺 models/tinyroberta        # Model files (ignored in Git)
 ┓ 📺 .devcontainer             # Dev container setup
 ┓ 📺 .venv                     # Virtual environment
 ┓ 📝 main.py                   # FastAPI service entry point
 ┓ 📝 test_main.py               # Pytest tests
 ┓ 📝 download_model.py          # Script to download the model
 ┓ 📝 requirements.txt           # Dependencies
 ┓ 📝 pyproject.toml             # Project config
 ┓ 📝 .pre-commit-config.yaml    # Pre-commit hooks config
 ┓ 📝 README.md                  # (You are here)
 ┗ 📝 .gitignore                 # Ignored files
```

## 🛠️ Setup Instructions
### 1️⃣ Clone the Repository
```
git clone https://github.com/cr-ejd/DSInternship.git
cd DSInternship
```

### 2️⃣ Set Up the Virtual Environment
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Download the Model
Run the script to download the Hugging Face model:
```
python download_model.py
```

### 4️⃣ Start the FastAPI Server
```
uvicorn main:app --reload
```
Now, open your browser and go to:
📌 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** to access the API.

## 🥪 Running Tests
Run tests using **pytest**:
```
pytest --cov=main
```

## ⚡ Pre-commit Hooks
Ensure all hooks pass before committing:
```
pre-commit run --all-files
```

## 🐜 License
This project is licensed under the **MIT License**.
