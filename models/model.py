import torch
from transformers import pipeline


def get_transcription(audio_path, lang, input_model, input_processor):
    pipe = pipeline(
        "automatic-speech-recognition",
        model=input_model,
        tokenizer=input_processor.tokenizer,
        feature_extractor=input_processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=True,
        torch_dtype=torch.float32,
        device="cpu",
    )
    result = pipe(audio_path, generate_kwargs={"language": lang})
    return result['text'].strip()
