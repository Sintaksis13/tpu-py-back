from dataclasses import dataclass
from typing import List

from app.domain.rich_order_line import RichOrderLine
from app.domain.customer_data import CustomerData

@dataclass(frozen=True)
class RichOrder:
    id: str
    orderLines: List[RichOrderLine]
    totalAmount: float
    customerData: CustomerData