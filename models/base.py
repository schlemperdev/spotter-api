from dataclasses import dataclass


@dataclass
class BaseEntity:
    cpfCnpj: str
    name: str
    sdrEmail: str
    ddiPhone: str
    phone: str
    address: str
    addressComplement: str
    zipcode: str
    city: str
    state: str
    country: str
