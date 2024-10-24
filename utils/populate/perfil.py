import requests
import json
import random

def populate_perfil():
    url_perfil = "http://127.0.0.1:8000/api/perfil/perfil/"
    url_sub_area = "http://127.0.0.1:8000/api/perfil/subArea/"
    url_area = "http://127.0.0.1:8000/api/perfil/area/"
    url_nacionality = "http://127.0.0.1:8000/api/perfil/nacionality/"    

    try:
        response_area = requests.get(url_area).json()
        response_sub_area = requests.get(url_sub_area).json()
        response_nacionality = requests.get(url_nacionality).json()
    except BaseException as error:
        print(error)

    id_choiced = random.randint(1, 100)

    area_choiced = [data.get('name') for data in response_area if data.get('id') == id_choiced]
    print(area_choiced)
    sub_area_choiced = [data.get('name') for data in response_sub_area if data.get('id') == id_choiced]
    print(sub_area_choiced)
    nacionality = [data.get('name') for data in response_nacionality if data.get('id') == id_choiced]
    print(nacionality)
    if not area_choiced or not sub_area_choiced or not nacionality:
        return f"Não foi encontrado nenhum dado com o ID {id_choiced}"

    data = {
        'Balance': random.randint(100, 100000),
        'price_per_hour': random.randint(10, 10000),
        'about_me': "I'm a young developer",
        'user': 1, 
        'nacionality': nacionality[0],  
        'photo': 'dfbf234b-0bed-4922-85a3-879c5207c981',
        'area': area_choiced[0],
        'sub_area': sub_area_choiced[0]
    }

    try:
        perfil_response = requests.post(url_perfil, json=data)
        print(perfil_response)
        if perfil_response.status_code == 201:
            print("Perfil criado com sucesso!")
        else:
            print(f"Erro ao criar o perfil: {perfil_response.status_code}")
    except BaseException as error:
        print(error)

    return True

for _ in range(35):
    if not populate_perfil():
        break
