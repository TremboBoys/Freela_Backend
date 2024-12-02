import requests

def ai_translate(text, target_language):
    if target_language == "English":
        target_language = "en"
    print(text)
    print(target_language)
        
    data = {
        "text": text,
        "target_language": target_language
    }
    print(data)
    
    try:
        response = requests.post("http://127.0.0.1:8090/ai", json=data)
    except BaseException as error:
        print("Error!")
        
    if response.status_code == 200:
        resp = response.json()
        print(resp['translated_text'])
        return resp['translated_text']
    else:
        print("Error in second plane!")
        
        
