from dataclasses import asdict
from models.contact import Contact
from serializers.contact_serializer import ContactSerializer
from api_requests.crm_api import create_contact


def handle_contact(contact_data, lead_id):
    try:
        contact = Contact(**contact_data, leadId=lead_id)

        contact_json = ContactSerializer.serialize(contact)

        response = create_contact(contact_json)

        return response

    except Exception as e:
        print(f"Erro ao processar o contato: {e}")
        return None
