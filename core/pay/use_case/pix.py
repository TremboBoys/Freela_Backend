import requests
from core.pay.models import Address, Transaction
from core.proposal.models import AcceptProposal


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
    

def create_transaction(objeto: dict):
    user = Address.objects.filter(perfil__user__email=objeto['email_payer']).first()
    if not user:
        raise ValueError("Usuário não existe")
    if 'project_id' in objeto:
        project = AcceptProposal.objects.filter(proposal__pk=objeto['project_id']).first()
        if not project:
            raise ValueError('Proposta para esse projeto não encontrado')
        
        del objeto['project_id']
        del object['project_name']
        try:
            response = requests.post(f"{urlpix}/transaction", json=objeto)
            response.raise_for_status()
        except requests.RequestException as error:
            return {"error": f"There is an error in the external service: {error}"}

        resp = response.json()
        transaction = Transaction.objects.create(id_transaction=resp['id_transaction'], user=user.perfil, accept_proposal=project, amount=objeto['transaction_amount'], method=objeto['payment_method_id'], number=objeto['number'])
        transaction.save()
        return resp
    if 'service_id' in objeto:
        pass
        
        

                        
            
        
            
        
        
        
        
            

    
    

