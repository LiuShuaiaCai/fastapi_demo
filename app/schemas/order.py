"""Order Schemas"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class OrderBase(BaseModel):
    """Base order schema"""

    user_id: int
    product_id: int
    quantity: int = Field(..., gt=0)
    total_price: float = Field(..., gt=0)


class OrderCreate(OrderBase):
    """Order creation schema"""

    pass


class OrderUpdate(BaseModel):
    """Order update schema"""

    status: Optional[str] = Field(None, pattern="^(pending|confirmed|shipped|delivered)$")
    quantity: Optional[int] = Field(None, gt=0)


class OrderResponse(OrderBase):
    """Order response schema"""

    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
