from dataclasses import dataclass, field


@dataclass
class Contact:
    leadId: str = field(default=None)  # ID do ao qual será vinculado
    contactEmail: str = field(default=None)
    contactName: str = field(default=None)
    ddiPhone1: str = field(default=None)
    phone1: str = field(default=None)
