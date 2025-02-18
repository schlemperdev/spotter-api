from forms.mainForm import data_collect, contact_data_collect
from controllers.OrganizationController import handle_org
from controllers.LeadController import handle_lead
from controllers.ContactController import handle_contact
from utils.data_splitter import split_data_for_entities


def main():
    print('Iniciando Cadastro de Lead e Organização. Por favor digite os dados solicitados abaixo:\n')

    main_data = data_collect()

    # Automatically split the relevant fields
    organization_data, lead_data = split_data_for_entities(main_data)

    # Handle Organization
    organization_id = str(handle_org(organization_data))
    if not organization_id:
        return
    print('ID da Organização:', organization_id)

    # Handle Lead
    lead_id = handle_lead(lead_data, organization_id)
    if not lead_id:
        print('Erro ao cirar o lead')
        return
    print('\n Lead Criado! Crie o contato com os dados solicitados abaixo:\n')

    contact_data = contact_data_collect()

    # Handle Contact
    contact_response = handle_contact(contact_data, lead_id)
    if contact_response:
        print('Contato criado com sucesso!')
    else:
        print('Erro ao criar o contato')


if __name__ == "__main__":
    main()
