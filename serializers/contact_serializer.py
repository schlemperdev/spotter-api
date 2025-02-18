from serializers.base_serializer import BaseSerializer


class ContactSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, contact):
        """Serializes a Contact instance."""
        return super().serialize(contact)
