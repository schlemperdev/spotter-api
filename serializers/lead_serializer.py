from serializers.base_serializer import BaseSerializer


class LeadSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, lead):
        """Serializes a Lead instance with additional static fields."""
        return {
            "duplicityValidation": True,
            "lead": super().serialize(lead)
        }
