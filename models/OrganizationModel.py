from models.BaseEntity import BaseEntity


class Organization(BaseEntity):
    def __init__(self, cpfCnpj, name, sdrEmail, ddiPhone, phone,
                 address, addressComplement, zipcode, city,
                 state, country):
        super().__init__(cpfCnpj, name, sdrEmail, ddiPhone, phone,
                         address, addressComplement, zipcode, city,
                         state, country)
        self.organizationId = None
