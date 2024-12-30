

import app.main as session
from app.params import audio_sample_rate

def get_audio_transcription(audio_data: list[float]):
    input_features = session.processor(audio_data, sampling_rate=audio_sample_rate, return_tensors="pt").input_features
    predicted_ids = session.model.generate(input_features)
    return session.processor.batch_decode(predicted_ids, skip_special_tokens=True)