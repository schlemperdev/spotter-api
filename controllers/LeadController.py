from models.LeadModel import Lead
from serializers.serializer import LeadSerializer
from api_requests.crm_api import create_lead

def handle_lead(main_data, organization_id):
    lead = Lead(
        cpfCnpj=main_data["cpfCnpj"],
        name=main_data["name"],
        sdrEmail=main_data["sdrEmail"],
        ddiPhone=main_data["ddiPhone"],
        phone=main_data["phone"],
        address=main_data["address"],
        addressNumber=main_data["addressNumber"],
        addressComplement=main_data["addressComplement"],
        neighborhood=main_data["neighborhood"],
        zipcode=main_data["zipcode"],
        city=main_data["city"],
        state=main_data["state"],
        country=main_data["country"],
        industry=main_data["industry"],
        source=main_data["source"],
        subSource=main_data["subSource"],
        organizationId=organization_id,
        funnelId=main_data["funnelId"],
        stage=main_data["stage"]
    )

    lead_json = LeadSerializer.serialize(lead)
    lead_json["lead"] = {key: value for key, value in lead_json["lead"].items() if value}

    response = create_lead(lead_json)

    if response is not None and "value" in response:
        return response["value"]
    else:
        print("Erro ao obter 'leadId' da resposta:" , response)
        return None