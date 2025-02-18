import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("SPOTTER_API_KEY")
BASE_URL = os.getenv("SPOTTER_BASE_URL")

# Verifica se as variáveis foram carregadas corretamente
if not API_KEY or not BASE_URL:
    raise ValueError(
        "Erro: SPOTTER_API_KEY ou SPOTTER_BASE_URL não definidos no .env")

HEADERS = {"Content-Type": "application/json", "token_exact": API_KEY}


def handle_response(response):
    """ Handles API response and errors """
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {response.status_code} - {err}")
    except requests.exceptions.RequestException as err:
        print(f"Erro de conexão: {err}")
    except requests.exceptions.JSONDecodeError:
        print("Erro: Resposta não é um JSON válido.")
    return None

# ORGANIZATION


def get_orgId(org_json):
    """ Fetches an organization ID by CNPJ. """
    url = f"{BASE_URL}/organization?$filter=cpfCnpj eq '{org_json["organization"]["cpfCnpj"]}'"
    return handle_response(requests.get(url, headers=HEADERS))


def create_org(org_json):
    """ Creates an organization. """
    url = f"{BASE_URL}/organizationAdd"
    return handle_response(requests.post(url, json=org_json, headers=HEADERS))

# LEAD


def create_lead(lead_json):
    """ Creates a lead. """
    url = f"{BASE_URL}/LeadsAdd"
    return handle_response(requests.post(url, json=lead_json, headers=HEADERS))

# CONTACT


def create_contact(contact_json):
    """ Creates a contact """
    url = f"{BASE_URL}/personsAdd"
    return handle_response(requests.post(url, json=contact_json, headers=HEADERS))
