from transformers import AutoModelForQuestionAnswering, AutoTokenizer

MODEL_NAME = "deepset/tinyroberta-squad2"
SAVE_PATH = "./models/tinyroberta"

# Download model & tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForQuestionAnswering.from_pretrained(MODEL_NAME)

# Save locally
tokenizer.save_pretrained(SAVE_PATH)
model.save_pretrained(SAVE_PATH)

print(f"✅ Model saved to {SAVE_PATH}")
