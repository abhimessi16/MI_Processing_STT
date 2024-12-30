from transformers import WhisperProcessor, WhisperForConditionalGeneration
from fastapi import FastAPI
import uvicorn

from app.routes.stt_route import stt_router

processor = WhisperProcessor.from_pretrained("openai/whisper-small", language="en", task="transcribe")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
model.config.forced_decoder_ids = None

app = FastAPI()
app.include_router(stt_router)