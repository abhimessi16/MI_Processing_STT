from pydantic import BaseModel

class STTRequest(BaseModel):
    stt_input: list[float]