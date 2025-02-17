from models.OrganizationModel import Organization
from serializers.serializer import OrganizationSerializer
from api_requests.crm_api import create_org

def handle_org(main_data):
    org = Organization(
        cpfCnpj=main_data["cpfCnpj"],
        name=main_data["name"],
        sdrEmail=main_data["sdrEmail"],
        ddiPhone=main_data["ddiPhone"],
        phone=main_data["phone"],
        address=main_data["address"],
        addressComplement=main_data["addressComplement"],
        zipcode=main_data["zipcode"],
        city=main_data["city"],
        state=main_data["state"],
        country=main_data["country"]
    )

    org_json = OrganizationSerializer.serialize(org)
    response = create_org(org_json)
    
    return response.get("organizationId")