import json

from fastapi import APIRouter, status
from fastapi.responses import Response

from app.models import STTRequest
from app.utils import get_audio_transcription

stt_router = APIRouter(prefix="/api/v1")

@stt_router.post("/stt")
async def speech_to_text(stt_request: STTRequest):
    try:
        audio_transcription = get_audio_transcription(stt_request.stt_input)
        print(audio_transcription, len(stt_request.stt_input))
        return Response(
            status_code=status.HTTP_200_OK,
            content=audio_transcription[0])
    except Exception as ex:
        return Response(content=json.dumps({
            "message": "Error during transcription."
        }), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)