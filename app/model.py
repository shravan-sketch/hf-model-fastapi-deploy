from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def load_model():
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    return tokenizer, model, pipe

def predict(text, tokenizer, model, pipe):
    result = pipe(text)
    return result[0]
