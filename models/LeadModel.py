from models.BaseEntity import BaseEntity


class Lead(BaseEntity):
    def __init__(self, cpfCnpj, name, sdrEmail, ddiPhone, phone, address,
                 addressNumber, addressComplement, neighborhood, zipcode,
                 city, state, country, industry, source, subSource,
                 organizationId, funnelId, stage):
        super().__init__(cpfCnpj, name, sdrEmail, ddiPhone, phone, address,
                         addressNumber, addressComplement, neighborhood, zipcode,
                         city, state, country)
        self.leadId = None
        self.industry = industry
        self.source = source
        self.subSource = subSource
        self.organizationId = organizationId
        self.description = None
        self.funnelId = funnelId
        self.stage = stage
        self.customId01 = None
        self.customId02 = None

    # def to_dict(self):
    #     return {
    #         "name": self.name,
    #         "industry": self.industry,
    #         "source": self.source,
    #         "subSource": self.subSource,
    #         "organizationId": self.organizationId,
    #         "sdrEmail": self.sdrEmail,
    #         "ddiPhone": self.ddiPhone,
    #         "phone": self.phone,
    #         "address": self.address,
    #         "addressNumber": self.addressNumber,
    #         "addressComplement": self.addressComplement,
    #         "neighborhood": self.neighborhood,
    #         "zipcode": self.zipcode,
    #         "city": self.city,
    #         "state": self.state,
    #         "country": self.country,
    #         "description": self.description,
    #         "cpfcnpj": self.cpfCnpj,
    #         "funnelId": self.funnelId,
    #         "stage": self.stage,
    #         "camposPersonalizados": [
    #             {"id": "customId01", "valor": self.id01},
    #             {"id": "customId02", "valor": self.id02}
    #         ]
    #     }
