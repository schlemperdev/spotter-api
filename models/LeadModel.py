from models.BaseEntity import BaseEntity


class Lead(BaseEntity):
    def __init__(self, cpfCnpj, name, sdrEmail, ddiPhone, phone, address, addressNumber, addressComplement, neighborhood, zipcode, city, state, country, industry, source, subSource, organizationId, funnelId, stage):
        super().__init__(cpfCnpj, name, sdrEmail, ddiPhone, phone, address, addressComplement, zipcode, city, state, country)
        self.leadId = None
        self.addressNumber = addressNumber
        self.neighborhood = neighborhood
        self.industry = industry
        self.source = source
        self.subSource = subSource
        self.organizationId = organizationId
        self.description = None
        self.funnelId = funnelId
        self.stage = stage
        self.customId01 = None
        self.customId02 = None
