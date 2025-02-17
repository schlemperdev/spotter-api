import json


class LeadSerializer:
    @staticmethod
    def serialize(lead):
        return json.dumps({
            "name": lead.name,
            "industry": lead.industry,
            "source": lead.source,
            "subSource": lead.subSource,
            "organizationId": lead.organizationId,
            "sdrEmail": lead.sdrEmail,
            "ddiPhone": lead.ddiPhone,
            "phone": lead.phone,
            "address": lead.address,
            "addressNumber": lead.addressNumber,
            "addressComplement": lead.addressComplement,
            "neighborhood": lead.neighborhood,
            "zipcode": lead.zipcode,
            "city": lead.city,
            "state": lead.state,
            "country": lead.country,
            "description": lead.description,
            "cpfcnpj": lead.cpfCnpj,
            "funnelId": lead.funnelId,
            "stage": lead.stage,
            "camposPersonalizados": [
                {"id": "customId01", "valor": lead.id01},
                {"id": "customId02", "valor": lead.id02}
            ]
        })


class ContactSerializer:
    @staticmethod
    def serialize(contact):
        return json.dumps({
            "E-mail": contact.contactEmail,
            "Name": contact.contactName,
            "leadId": contact.leadId,
            "ddiPhone1": contact.ddiPhone1,
            "phone1": contact.phone1,
            "mainContact": True
        })


class OrganizationSerializer:
    @staticmethod
    def serialize(org):
        return ({
            "duplicityValidation": False,
            "organization": {    
                "name": org.name,
                "userEmail": org.sdrEmail,
                "cpfCnpj": org.cpfCnpj,
                "ddiPhone": org.ddiPhone,
                "phone": org.phone,
                "address": org.address,
                "addressComplement": org.addressComplement,
                "zipcode": org.zipcode,
                "city": org.city,
                "state": org.state,
                "country": org.country
            }
        })
