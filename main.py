import os
from functools import lru_cache
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

app = FastAPI()

MODEL_DIR = "./models/tinyroberta"
MODEL_FILE = os.path.join(MODEL_DIR, "model.safetensors")

if not os.path.exists(MODEL_FILE):
    print("Downloading model...")
    os.system("python download_model.py")


class QAInput(BaseModel):
    question: str
    context: str


@lru_cache(maxsize=1)
def get_pipeline():
    """Lazy loads the model only once"""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForQuestionAnswering.from_pretrained(MODEL_DIR)
    return pipeline("question-answering", model=model, tokenizer=tokenizer)


@app.get("/")
def home():
    return {"message": "Welcome to the QA API"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.post("/predict")
def predict(data: QAInput):
    qa_pipeline = get_pipeline()
    result = qa_pipeline(question=data.question, context=data.context)
    return {"answer": result["answer"], "score": result["score"]}
