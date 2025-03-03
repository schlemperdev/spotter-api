from dataclasses import asdict
from models.lead import Lead
from serializers.lead_serializer import LeadSerializer
from api_requests.crm_api import create_lead


def handle_lead(lead_data, organization_id):
    """ Handles lead creation and gets ID """
    try:
        lead = Lead(**lead_data, organizationId=organization_id)

        lead_json = LeadSerializer.serialize(lead)

        response = create_lead(lead_json)

        if response and "value" in response:  # Returns Lead ID
            return response["value"]

        print("Erro ao obter 'leadId' da resposta:", response)
        return None

    except Exception as e:
        print(f"Erro ao processar o lead: {e}")
        return None
