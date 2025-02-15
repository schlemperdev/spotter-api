class ContactModel:
    def __init__(self, email, name, leadId, ddiPhone1, phone1, mainContact):
        self.contactEmail = contactEmail
        self.contactName = contactName
        self.leadId = leadId
        self.ddiPhone1 = ddiPhone1
        self.phone1 = phone1
        self.mainContact = mainContact
    
    def to_dict(self):
        return {
            "E-mail": self.contactEmail,
            "Name": self.contactName,
            "leadId": self.leadId,
            "ddiPhone1": self.ddiPhone1,
            "phone1": self.phone1,
            "mainContact": self.mainContact
        }
