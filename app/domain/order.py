from dataclasses import dataclass
from typing import List

from app.domain.order_line import OrderLine
from app.domain.customer_data import CustomerData

@dataclass(frozen=True)
class Order:
    id: str
    orderLines: List[OrderLine]
    totalAmount: float
    customerData: CustomerData