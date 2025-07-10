from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.model import load_model, predict

app = FastAPI()
tokenizer, model, pipeline_fn = load_model()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def get_prediction(data: TextInput):
    result = predict(data.text, tokenizer, model, pipeline_fn)
    return {"prediction": result}

