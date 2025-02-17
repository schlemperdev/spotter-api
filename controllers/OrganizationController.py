from models.OrganizationModel import Organization
from serializers.serializer import OrganizationSerializer
from api_requests.crm_api import create_org, get_orgId

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
    org_json["organization"] = {key: value for key, value in org_json["organization"].items() if value}

    response = get_orgId(org_json)

    if "value" in response and len(response["value"]) > 0:
        return response["value"][0]["id"]
    else:
        print("Erro ao obter 'id' da organização: ", response)
        print("Você deseja criar uma nova organização com este CNPJ: ", org_json["organization"]["cpfCnpj"], "?")
        proceed = input("Digite sim ou nao. Esta operação não é reversível\n")

        if proceed == "sim":
            response = create_org(org_json)

            if "value" in response and len(response["value"]) > 0:
                return response["value"][0]["id"]
            else:
                print("Erro: ", response)
                return None

        else:
            print("Cadastro interrompido pelo usuário.")
            exit