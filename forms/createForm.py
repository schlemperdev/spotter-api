def data_collect():
    print("Cadastro Geral:")
    return {
        "cpfCnpj": input("CPF/CNPJ: "),
        "name": input("Nome do Lead: "),
        "sdrEmail": "renan.schlemper@brasilrad.com.br",
        "ddiPhone": "55",
        "phone": input("Telefone: "),
        "address": input("Endereço: "),
        "addressNumber": input("Número: "),
        "addressComplement": input("Complemento: "),
        "neighborhood": input("Bairro: "),
        "zipcode": input("CEP: "),
        "city": input("Cidade: "),
        "state": input("Estado: "),
        "country": input("País: "),
        "industry": input("Setor: "),
        "source": input("Origem: "),
        "subSource": input("Sub-origem: "),
        "funnelId": input("ID do Funil: "),
        "stage": input("Etapa: "),
    }


def contact_data_collect():
    print("Cadastro de Contato:")
    return {
        "contactName": input("Nome do Contato: "),
        "contactEmail": input("E-mail: "),
        "ddiPhone1": "55",
        "phone1": input("Telefone: ")
    }
