from dataclasses import dataclass, field
from models.base import BaseEntity


@dataclass
class Organization(BaseEntity):
    organizationId: str = field(default=None)
