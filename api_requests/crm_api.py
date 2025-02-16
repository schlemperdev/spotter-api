import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv("SPOTTER_API_KEY")
BASE_URL = os.getenv("SSPOTER_BASE_URL")


def create_lead(lead_json):
    response = requests.post(f"{BASE_URL}/LeadsAdd",
                             data=lead_json,
                             headers={"Content-Type": "application/json",
                                      "token_exact": f"{API_KEY}"})
    return response.json()


def create_contact(contact_json):
    response = requests.post(f"{BASE_URL}/organizationAdd",
                             data=contact_json,
                             headers={"Content-Type": "application/json",
                                      "token_exact": f"{API_KEY}"})
    return response.json()


def create_org(org_json):
    response = requests.post(f"{BASE_URL}/personsAdd",
                             data=org_json,
                             headers={"Content-Type": "application/json",
                                      "token_exact": f"{API_KEY}"})
    return response.json()
