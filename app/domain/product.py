from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    id: str
    title: str
    description: str
    price: float