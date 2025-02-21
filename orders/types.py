
from pydantic import BaseModel
from typing import List, Optional

class OrderRequestEntity(BaseModel):
    user_id: int
    order_id: Optional[int]
    item_ids: Optional[List[int]]
    total_amount: Optional[float]