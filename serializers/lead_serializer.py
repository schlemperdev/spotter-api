from serializers.base_serializer import BaseSerializer


class LeadSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, lead):
        """Serializes a Lead instance with additional static fields."""
        lead_dict = 

        if "cpfCnpj" in lead_data:      #Renames cpfCnpj to cpfcnpj
            lead_data["cpfcnpj"] = lead_data.pop("cpfCnpj")

        if "userEmail" in lead_data:    #Renames userEmail to sdrEmail
            lead_data["sdrEmail"] = lead_data.pop("userEmail")

        return {
            "duplicityValidation": True,
            "lead": super().serialize(lead_data)
        }
