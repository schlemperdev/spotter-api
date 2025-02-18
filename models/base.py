from dataclasses import dataclass


@dataclass
class BaseEntity:
    cpfCnpj: str
    name: str
    userEmail: str
    ddiPhone: str
    phone: str
    address: str
    addressComplement: str
    zipcode: str
    city: str
    state: str
    country: str
