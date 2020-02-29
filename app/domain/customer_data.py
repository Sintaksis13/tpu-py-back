from dataclasses import dataclass

@dataclass(frozen=True)
class CustomerData:
    name: str
    address: str
    phone: str