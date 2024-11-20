import requests

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
    response = requests.post(f"{urlpix}/address", json=data)
    
    if response.status_code == 200:
        return True
    else:
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

result = get_address(email="joaovictor239090@gmail.com")
print(result)
    
    
    
        