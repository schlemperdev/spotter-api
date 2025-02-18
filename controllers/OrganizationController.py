from dataclasses import asdict
from models.organization import Organization
from serializers.organization_serializer import OrganizationSerializer
from api_requests.crm_api import create_org, get_orgId


def get_user_confirmation(prompt):
    """Helper function to get a yes/no confirmation for the user."""
    while True:
        response = input(f"{prompt} (sim/não): ").strip().lower()
        if response in ["sim", "não", "nao"]:
            return response == "sim"
        print("Resposta inválida. Digite 'sim' ou 'não'.")


def handle_org(organization_data):
    """ Handles organization lookup or creation """
    try:
        org = Organization(**organization_data)

        org_json = OrganizationSerializer.serialize(org)

        response = get_orgId(org_json)

        # Retruns Org ID
        if response and "value" in response and response["value"]:
            return response["value"][0]["id"]

        print("Erro ao obter 'id' da organização: ", response)

        if get_user_confirmation(f'Você deseja criar uma nova organização com CNPJ {org_json["organization"]["cpfCnpj"]}?'):
            input(org_json)  ###debugging
            response = create_org(org_json)
            if response and "value" in response and response["value"]:
                return response["value"][0]["id"]
            print("Erro ao criar a organização:", response)
            return None

    except Exception as e:
        print(f"Erro ao processar a organização: {e}")
        return None
