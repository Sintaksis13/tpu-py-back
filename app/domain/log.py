import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class Log:
    id: str
    date: datetime
    message: str