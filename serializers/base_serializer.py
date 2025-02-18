class BaseSerializer:
    """Base serializer that can automatically convert objects to JSON-compatible dictionaries."""

    @staticmethod
    def clean_dict(data):
        """Removes None values from a dictionary."""
        return {k: v for k, v in data.items() if v is not None}

    @classmethod
    def serialize(cls, obj, extra_data=None):
        """ Serializes an object by automatically filtering out None values. Supports additional static fields. """
        data = cls.clean_dict(data)  # Remove None values

        # Merge extra_data if provided
        if extra_data:
            data.update(extra_data)

        return data
