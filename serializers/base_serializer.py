class BaseSerializer:
    """Base serializer that can automatically convert objects to JSON-compatible dictionaries."""

    @classmethod
    def serialize(cls, obj, extra_data=None):
        """ Serializes an object by automatically filtering out None values. Supports additional static fields. """
        return {k: v for k, v in asdict(obj).items() if v is not None}