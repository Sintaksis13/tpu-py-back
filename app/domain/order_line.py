from dataclasses import dataclass

@dataclass(frozen=True)
class OrderLine:
    productId: str
    count: int