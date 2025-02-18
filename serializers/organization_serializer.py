from serializers.base_serializer import BaseSerializer


class OrganizationSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, org):
        """Serializes an Organization instance with additional static fields."""
        return {
            "duplicityValidation": True,
            "organization": super().serialize(org)
        }
