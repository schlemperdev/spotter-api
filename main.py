from forms.mainForm import data_collect, contact_data_collect
from controllers.OrganizationController import handle_org
from controllers.LeadController import handle_lead
from controllers.ConctactController import handle_contact

def main():
    print ('Iniciando Cadastro de Lead e Organização. Por favor digite os dados solicitados abaixo:\n')
    main_data = data_collect()

    print(main_data)
    input('digite 1 para continuar')

    organization_id = handle_org(main_data)
    if not organization_id:
        print('Erro ao criar organização')
        return
    
    lead_id = handle_lead(main_data, organization_id)
    if not lead_id:
        print('Erro ao cirar o lead')
        return
    
    print('\n Lead Criado! Crie o contato com os dados solicitados abaixo:\n')
    contact_data = contact_data_collect()

    contact_response = handle_contact(contact_data, lead_id)
    if contact_response:
        print('Contato criado com sucesso!')
    else:
        print('Erro ao criar o contato')

if __name__ == "__main__":
    main()