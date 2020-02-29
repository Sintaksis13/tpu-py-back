from dataclasses import dataclass

from app.domain.product import Product

@dataclass(frozen=True)
class RichOrderLine:
    product: Product
    count: int