class Contact:
    def __init__(self, leadId, contactEmail, contactName, ddiPhone1, phone1):
        self.leadId = leadId  # ID do ao qual será vinculado
        self.contactEmail = contactEmail
        self.contactName = contactName
        self.ddiPhone1 = ddiPhone1
        self.phone1 = phone1

    # def to_dict(self):
    #     return {
    #         "E-mail": self.contactEmail,
    #         "Name": self.contactName,
    #         "leadId": self.leadId,
    #         "ddiPhone1": self.ddiPhone1,
    #         "phone1": self.phone1,
    #         "mainContact": "TRUE"
    #     }
