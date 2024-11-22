import requests
from core.pay.models import Address

urlpix = "https://ms-pix.onrender.com"


def create_address(street_name, street_number, complement_address, cellphone_number, neighborhood_name, city_name, name_payer, email_payer, zip_code):
    data = {
        "street_name": street_name,
        "street_number": street_number,
        "complement_address": complement_address,
        "cellphone_number": cellphone_number,
        "neighborhood_name": neighborhood_name,
        "city_name": city_name,
        "name_payer": name_payer,
        "email_payer": email_payer,
        "zip_code": zip_code 
    }
    
    try:
        response = requests.post(f"{urlpix}/address", json=data)
        response.raise_for_status() 
        return True
    except requests.RequestException as e:
        print(f"Erro ao criar endereço: {e}")
        return False
    
def get_address(email):
    try:
        response = requests.get(f"{urlpix}/address/{email}")
        response.raise_for_status()  
    except requests.RequestException as error:
        return {"error": f"There is an error in the external service: {error}"}
    
    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid JSON received from external service"}

def update_address(id_address, street_name, street_number, complement_address, cellphone_number, neighborhood_name, city_name, name_payer, email_payer, zip_code):
    data = {
        "street_name": street_name,
        "street_number": street_number,
        "complement_address": complement_address,
        "cellphone_number": cellphone_number,
        "neighborhood_name": neighborhood_name,
        "city_name": city_name,
        "name_payer": name_payer,
        "email_payer": email_payer,
        "zip_code": zip_code 
    }
    
    try:
        response = requests.put(f"{urlpix}/address/{id_address}", json=data)
        response.raise_for_status() 
        return True
    except requests.RequestException as e:
        print(f"Erro ao criar endereço: {e}")
        return False
    
def get_address(email):
    try:
        response = requests.get(f"{urlpix}/transaction/{email}")
        response.raise_for_status()  
    except requests.RequestException as error:
        return {"error": f"There is an error in the external service: {error}"}
    
    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid JSON received from external service"}
    
result = get_address(email="joaovictor239090@gmail.com")
print(result)

def create_transaction(amount, method, email_payer, type_data, number):
    user = Address.objects.filter(perfil__user__email=email_payer).first
    if not user:
        raise ValueError("O email não procede")

    data = {
        "transaction_amount": amount,
        "payment_method_id": method,
        "payer": {
            "email": email_payer,
            "identification": {
                "type": type_data,
                "number": number
            }
        }
    }
    try:
        response = requests.post(f"{urlpix}/transaction", json=data)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ValueError(error)
    
    try:
        return response.json()
    except ValueError as error:
        raise ValueError(error)




