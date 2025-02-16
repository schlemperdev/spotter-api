class BaseEntity:
    def __init__(self, cpfCnpj, name, sdrEmail, ddiPhone, phone, address,
                 addressNumber, addressComplement, neighborhood, zipcode,
                 city, state, country):
        self.cpfCnpj = cpfCnpj
        self.name = name
        self.sdrEmail = sdrEmail
        self.ddiPhone = ddiPhone
        self.phone = phone
        self.address = address
        self.addressNumber = addressNumber
        self.addressComplement = addressComplement
        self.neighborhood = neighborhood
        self.zipcode = zipcode
        self.city = city
        self.state = state
        self.country = country
