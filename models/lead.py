from dataclasses import dataclass, field
from models.base import BaseEntity


@dataclass
class Lead(BaseEntity):
    leadId: str = field(default=None)
    addressNumber: str = field(default=None)
    neighborhood: str = field(default=None)
    industry: str = field(default=None)
    source: str = field(default=None)
    subSource: str = field(default=None)
    organizationId: str = field(default=None)
    description: str = field(default=None)
    funnelId: str = field(default=None)
    stage: str = field(default=None)
