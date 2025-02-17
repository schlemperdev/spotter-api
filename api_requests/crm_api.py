import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv("SPOTTER_API_KEY")
BASE_URL = os.getenv("SSPOTER_BASE_URL")

endpoint = ""
url = f"{BASE_URL}{endpoint}"
headers = {"Content-Type": "application/json", "token_exact": f"{API_KEY}"}


def create_org(org_json):
    endpoint = "/personsAdd"
    response = requests.post(url, data=org_json, headers=headers)
    if response.status_code == 201:
        return response.json()  # Retorna os dados da organização criada, incluindo o ID
    else:
        print(f"Erro ao criar organização: {response.status_code}")
        print(response.text)
        return None


def create_lead(lead_json):
    endpoint = "/LeadsAdd"
    response = requests.post(url, data=lead_json, headers=headers)
    if response.status_code == 201:
        return response.json()  # Retorna os dados do lead criado, incluindo o ID
    else:
        print(f"Erro ao criar lead: {response.status_code}")
        print(response.text)
        return None


def create_contact(contact_json):
    endpoint = "/personsAdd"
    response = requests.post(url, data=contact_json, headers=headers)
    if response.status_code == 201:
        return response.json()  # Retorna os dados do contato criado
    else:
        print(f"Erro ao criar lead: {response.status_code}")
        print(response.text)
        return None
