from transformers import pipeline

# Carregar o pipeline de tradução
translator = pipeline("translation_en_to_fr")  # Tradução do inglês para o francês

# Texto a ser traduzido
text_to_translate = "Hello, how are you?"

# Realizando a tradução
translation = translator(text_to_translate)

# Exibindo a tradução
print(translation[0]['translation_text'])
