from models.ContactModel import Contact
from serializers.serializer import ContactSerializer
from api_requests.crm_api import create_contact

def handle_contact(contact_data, lead_id):
    contact = Contact(
        leadId=lead_id,
        contactEmail=contact_data["contactEmail"],
        contactName=contact_data["contactName"],
        ddiPhone1=contact_data["ddiPhone1"],
        phone1=contact_data["phone1"]
    )

    contact_json = ContactSerializer.serialize(contact)
    response = create_contact(contact_json)

    return response