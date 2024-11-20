import requests
from core.pay.models import Address
from core.user.models import User

urlpix = "http://localhost:3000"


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

def update_address(id_address, street_name, street_number, complement_address, cellphone_number, neighborhood_name, city_name, name_payer, email_payer, zip_code, old_email):
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
    
    user = User.objects.filter(email=old_email).first()
    
    if not user:
        return 404
    
    if user.email != email_payer:
        user.email = email_payer
        user.save()
    
    user = User.objects.update_or_create(
        perfil__user=user,
        defaults={
            "street_name": street_name,
            "street_number": street_number,
            "complement_address": complement_address,
            "cellphone_number": cellphone_number,
            "neighborhood_name": neighborhood_name,
            "city_name": city_name,
            "name_payer": name_payer,
            "zip_code": zip_code 
        }
    )
    try:
        response = requests.put(f"{urlpix}/address/{id_address}", json=data)
        response.raise_for_status() 
        return True
    except requests.RequestException as e:
        print(f"Erro ao criar endereço: {e}")
        return False
    

    
    
    
    
    
    
    
    
        