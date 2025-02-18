from models.OrganizationModel import Organization
from serializers.serializer import OrganizationSerializer
from api_requests.crm_api import create_org, get_orgId

def get_user_confirmation(prompt):
    """Helper function to get a yes/no confirmation for the user."""
    while True:
        response = input(f"{prompt} (sim/não): ").strip().lower()
        if response in ["sim", "não", "nao"]:
            return response == "sim"
        print("Resposta inválida. Digite 'sim' ou 'não'.")

def handle_org(main_data):
    """ Handles organization lookup or creation """
    try:
        org = Organization(**main_data)
        
        org_json = OrganizationSerializer.serialize(org)
        org_json["organization"] = {key: value for key, value in org_json["organization"].items() if value}

        response = get_orgId(org_json)

        if response and "value" in response and response["value"]: ##Retruns Org ID
            return response["value"][0]["id"]

        print("Erro ao obter 'id' da organização: ", response)
        
        if get_user_confirmation(f"Você deseja criar uma nova organização com CNPJ {org_json["organization"]["cpfCnpj"]}?"):
            response = create_org(org_json)
            if response and "value" in response and response["value"]:
                return response["value"][0]["id"]
            print("Erro ao criar a organização:", response)

        print("Cadastro interrompido pelo usuário.")
        return None
        
    except Exception as e:
        print(f"Erro ao processar a organização: {e}")
        return None