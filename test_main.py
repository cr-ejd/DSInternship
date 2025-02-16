from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)


# Test the home route
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the QA API"}


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


def mock_pipeline(question, context):
    return {"answer": "42", "score": 1.0}


# Test the /predict route with mocking the model pipeline
@patch("main.get_pipeline")
def test_predict(mock_get_pipeline):
    mock_get_pipeline.return_value = mock_pipeline

    data = {
        "question": "What is the answer to life?",
        "context": "The answer to life, the universe, and everything is 42.",
    }
    response = client.post("/predict", json=data)

    assert response.status_code == 200
    assert response.json() == {"answer": "42", "score": 1.0}
