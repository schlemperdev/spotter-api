from dataclasses import dataclass, field


@dataclass
class Contact:
    leadId: str  # ID do ao qual será vinculado
    contactEmail: str
    contactName: str
    ddiPhone1: str
    phone1: str
