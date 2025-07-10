# hf-model-fastapi-deploy

# 🤗🖥️ FastAPI Deployment of Hugging Face Sentiment Model

<p align="center">
  <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="140" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="120" />
</p>

<p align="center">
  <b>Deploy a Hugging Face NLP model using FastAPI</b>
</p>

---

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![HuggingFace](https://img.shields.io/badge/HuggingFace-%F0%9F%A4%97-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-lightblue?style=for-the-badge&logo=docker)

---

## 🧠 Overview

This project demonstrates how to deploy a pre-trained sentiment analysis model from Hugging Face using **FastAPI**.  
It serves an endpoint that accepts text input and returns the **sentiment prediction** (`POSITIVE` or `NEGATIVE`) with a confidence score.

> 💬 Powered by: `distilbert-base-uncased-finetuned-sst-2-english`

---

## 🚀 Getting Started

You can run this project locally using Python or inside a Docker container.

---

### 🛠️ Run Locally (Dev Setup)

```bash
# 1. Clone the repo
git clone https://github.com/your-username/hf-model-fastapi-deploy.git
cd hf-model-fastapi-deploy

# 2. (Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 3. Install dependencies
pip install -r app/requirements.txt

# 4. Run the FastAPI app
uvicorn app.main:app --reload
