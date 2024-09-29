from transformers import pipeline

class TranslationService:
    def __init__(self):
        self.translator = pipeline("translation_en_to_fr")  # Tradução de inglês para francês

    def translate(self, text):
        result = self.translator(text, max_length=40)
        return result[0]['translation_text']
