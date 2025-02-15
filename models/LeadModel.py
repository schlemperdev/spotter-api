class LeadModel:
    def __init__(self, name, industry, source, subSource, organizationId, sdrEmail, ddiPhone, phone, address, addressNumber, addressComplement, neighborhood, zipcode, city, state, country, description, cpfCnpj, funnelId, stage, customfields):
        self.name = name
        self.industry = industry
        self.source = source
        self.subSource = subSource
        self.organizationId = organizationId
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
        self.description = description
        self.cpfCnpj = cpfCnpj
        self.funnelId = funnelId
        self.stage = stage
        self.customId01 = id01
        self.customId02 = id02
    
    def to_dict(self):
        return {
            "name": self.name,
            "industry": self.industry,
            "source": self.source,
            "subSource": self.subSource,
            "organizationId": self.organizationId,
            "sdrEmail": self.sdrEmail,
            "ddiPhone": self.ddiPhone,
            "phone": self.phone,
            "address": self.address,
            "addressNumber": self.addressNumber,
            "addressComplement": self.addressComplement,
            "neighborhood": self.neighborhood,
            "zipcode": self.zipcode,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "description": self.description,
            "cpfCnpj": self.cpfCnpj,
            "funnelId": self.funnelId,
            "stage": self.stage,
            "camposPersonalizados": [
                {"id": "customId01", "valor": self.id01},
                {"id": "customId02", "valor": self.id02}
            ]
        }
