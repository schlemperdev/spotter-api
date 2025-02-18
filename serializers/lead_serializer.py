from serializers.base_serializer import BaseSerializer
from dataclasses import asdict


class LeadSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, lead):
        """Serializes a Lead instance with additional static fields."""
        lead_dict = cls.clean_dict(asdict(lead))

        if "cpfCnpj" in lead_dict:      #Renames cpfCnpj to cpfcnpj
            lead_dict["cpfcnpj"] = lead_dict.pop("cpfCnpj")

        if "userEmail" in lead_dict:    #Renames userEmail to sdrEmail
            lead_dict["sdrEmail"] = lead_dict.pop("userEmail")

        return {
            "duplicityValidation": True,
            "lead": lead_dict
        }
