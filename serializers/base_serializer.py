import json
from dataclasses import asdict


class BaseSerializer:
    """Base serializer that can automatically convert objects to JSON-compatible dictionaries."""

    @classmethod
    def serialize(cls, obj):
        """ Serializes an object by automatically filtering out None values. Supports additional static fields. """
        return {k: v for k, v in asdict(obj).items() if v and v is not None}
