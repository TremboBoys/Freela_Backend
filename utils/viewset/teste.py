import requests


data = {
    "in_execution": False
}
response = requests.patch("http://127.0.0.1:8000/api/perfil/myProjects/1/", json=data)
print(response.status_code)
print(response.json())