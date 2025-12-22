from typing import Optional

from pydantic import BaseModel, Field
from typing import List

class Order(BaseModel):
    items: List[str] = Field(min_length=1)

order = Order(items=['3', '23', '344'])
print(order.items)