class OrganizationModel:
    def __init__(self, name, userEmail, cpfCnpj, ddiPhone, phone, address, addressComplement, zipcode, city, state, country):
        self.name = name
        self.userEmail = userEmail
        self.cpfCnpj = cpfCnpj
        self.ddiPhone = ddiPhone
        self.phone = phone
        self.address = address
        self.addressComplement = addressComplement
        self.zipcode = zipcode
        self.city = city
        self.state = state
        self.country = country
    
    def to_dict(self):
        return {
            "name": self.name,
            "userEmail": self.userEmail,
            "cpfCnpj": self.cpfCnpj,
            "ddiPhone": self.ddiPhone,
            "phone": self.phone,
            "address": self.address,
            "addressComplement": self.addressComplement,
            "zipcode": self.zipcode,
            "city": self.city,
            "state": self.state,
            "country": self.country
        }
