import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv("SPOTTER_API_KEY")
BASE_URL = os.getenv("SPOTTER_BASE_URL")

# Verifica se as variáveis foram carregadas corretamente
if not API_KEY or not BASE_URL:
    raise ValueError(
        "Erro: SPOTTER_API_KEY ou SPOTTER_BASE_URL não definidos no .env")

headers = {"Content-Type": "application/json", "token_exact": API_KEY}


def create_org(org_json):
    endpoint = "/organizationAdd"
    url = BASE_URL + endpoint

    response = requests.post(url, json=org_json, headers=headers)

    if response.status_code == 201:
        try:
            return response.json()  # Retorna os dados da organização criada, incluindo o ID
        except requests.exceptions.JSONDecodeError:
            print("Erro: Resposta não é um JSON válido.")
            return None
    else:
        print(f"Erro código: {response.status_code}")
        print("Resposta:", response.text)
        return None

def get_orgId(org_json):
    endpoint = "/organization"
    odataFilter = f"?$filter=cpfCnpj eq '{org_json["organization"]["cpfCnpj"]}'"

    url = BASE_URL + endpoint + odataFilter

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()
        except Exception as e:
            print(f"Error parsing response: {e}")
    else:
        print(f"Error while fetching organization: {response.status_code}")
        print(response.text)
        return None


def create_lead(lead_json):
    endpoint = "/LeadsAdd"
    url = BASE_URL + endpoint

    response = requests.post(url, json=lead_json, headers=headers)

    if response.status_code == 201:
        try:
            return response.json()  # Retorna os dados do lead criado, incluindo o ID
        except requests.exceptions.JSONDecodeError:
            print("Erro: Resposta não é um JSON válido.")
            return None
    else:
        print("Erro código: ", {response.status_code})
        print("Resposta: ", response.text)
        return None


def create_contact(contact_json):
    endpoint = "/personsAdd"
    url = BASE_URL + endpoint

    response = requests.post(url, json=contact_json, headers=headers)

    if response.status_code == 201:
        try:
            return response.json()  # Retorna os dados do contato criado.
        except requests.exceptions.JSONDecodeError:
            print("Erro: Resposta não é um JSON válido.")
            return None
    else:
        print(f"Erro código: {response.status_code}")
        print("Resposta:", response.text)
        return None
