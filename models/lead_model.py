class Lead:
    def __init__(self, leadName, industry, source, subSource, organizationId, sdrEmail, ddiPhone, phone, address, addressNumber, addressComplement, neighborhood, zipcode, city, state, country, description, cpfcnpj, funnelId, stage, customfields):
        self.leadId = None
        self.leadName = leadName
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
        self.cpfcnpj = cpfcnpj
        self.funnelId = funnelId
        self.stage = stage
        self.customId01 = id01
        self.customId02 = id02

    def to_dict(self):
        return {
            "name": self.leadName,
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
            "cpfcnpj": self.cpfcnpj,
            "funnelId": self.funnelId,
            "stage": self.stage,
            "camposPersonalizados": [
                {"id": "customId01", "valor": self.id01},
                {"id": "customId02", "valor": self.id02}
            ]
        }
