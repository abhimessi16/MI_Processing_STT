from transformers import WhisperProcessor, WhisperForConditionalGeneration
from fastapi import FastAPI

from app.routes.stt_route import stt_router

processor = WhisperProcessor.from_pretrained("openai/whisper-small", language="en", task="transcribe")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

app = FastAPI()
app.include_router(stt_router)