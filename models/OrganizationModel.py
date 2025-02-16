from models.BaseEntity import BaseEntity


class Organization(BaseEntity):
    def __init__(self, cpfCnpj, name, sdrEmail, ddiPhone, phone,
                 address, addressComplement, zipcode, city, 
                 state, country):
        super().__init__(cpfCnpj, name, sdrEmail, ddiPhone, phone,
                 address, addressComplement, zipcode, city, 
                 state, country)
        self.organizationId = None

    # def to_dict(self):
    #     return {
    #         "name": self.name,
    #         "userEmail": self.sdrEmail,
    #         "cpfCnpj": self.cpfCnpj,
    #         "ddiPhone": self.ddiPhone,
    #         "phone": self.phone,
    #         "address": self.address,
    #         "addressComplement": self.addressComplement,
    #         "zipcode": self.zipcode,
    #         "city": self.city,
    #         "state": self.state,
    #         "country": self.country
    #     }
