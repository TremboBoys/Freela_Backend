from transformers import pipeline
from langdetect import detect

def translante_text(text, target_language):
    translator = pipeline("translation", model="facebook/m2m100_418M")
    source_language = detect(text)
    result = translator(text, src_lang=source_language, tgt_lang=target_language, max_length=255)
    return result[0]['translation_text']
