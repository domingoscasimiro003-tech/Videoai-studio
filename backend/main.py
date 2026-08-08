import os
import requests

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(title="VideoAI Studio API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "VideoAI Studio API está funcionando"
    }


@app.post("/gerar")
def gerar_video(request: VideoRequest):

    prompt = request.prompt.strip()

    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="O prompt não pode estar vazio."
        )

    token = os.getenv("REPLICATE_API_TOKEN")

    if not token:
        raise HTTPException(
            status_code=500,
            detail="REPLICATE_API_TOKEN não configurado."
        )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "input": {
            "prompt": prompt
        }
    }

    response = requests.post(
        "https://api.replicate.com/v1/models/minimax/video-01/predictions",
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    data = response.json()

    return {
        "status": data.get("status"),
        "id": data.get("id"),
        "video": data.get("output"),
        "prediction_url": data.get("urls", {}).get("get")
    }
