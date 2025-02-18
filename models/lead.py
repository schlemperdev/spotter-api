from dataclasses import dataclass, field
from models.base import BaseEntity


@dataclass
class Lead(BaseEntity):
    leadId: str
    addressNumber: str
    neighborhood: str
    industry: str
    source: str
    subSource: str
    organizationId: str
    # description: str
    funnelId: int
    stage: str
