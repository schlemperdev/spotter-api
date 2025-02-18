from serializers.base_serializer import BaseSerializer


class ContactSerializer:
    @classmethod
    def serialize(cls, contact):
        """Serializes a Contact instance."""
        return {
            super().serialize(contact)
        }