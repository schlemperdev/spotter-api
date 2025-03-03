def data_collect():
    print("Cadastro Geral:")
    main_data = {
        "leadId": "",
        "cpfCnpj": input("CPF/CNPJ: "),
        "name": input("Nome do Lead: "),
        "userEmail": "renan.schlemper@brasilrad.com.br",
        "ddiPhone": input("DDI Telefone: "),
        "phone": input("Telefone: "),
        "address": input("Endereço: "),
        "addressNumber": input("Número: "),
        "addressComplement": input("Complemento: "),
        "neighborhood": input("Bairro: "),
        "zipcode": input("CEP: "),
        "city": input("Cidade: "),
        "state": input("Estado: "),
        "country": input("País: "),
        "industry": input("Mercado: "),
        "source": input("Origem: "),
        "subSource": input("Sub-origem: "),
        "funnelId": input("ID do Funil: "),
        "stage": input("Etapa: "),
    }
    return main_data


def contact_data_collect():
    print("Cadastro de Contato:")
    contact_data = {
        "contactName": input("Nome do Contato: "),
        "contactEmail": input("E-mail: "),
        "ddiPhone1": input("DDI Telefone: "),
        "phone1": input("Telefone: ")
    }
    return contact_data
