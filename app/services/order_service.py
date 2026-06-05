"""Order Service"""
from sqlalchemy.orm import Session
from typing import Optional, List

from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate


class OrderService:
    """Order business logic service"""

    @staticmethod
    def get_order(db: Session, order_id: int) -> Optional[Order]:
        """Get order by ID"""
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def get_orders(
        db: Session, user_id: Optional[int] = None, skip: int = 0, limit: int = 10
    ) -> List[Order]:
        """Get orders with optional user filter"""
        query = db.query(Order)
        if user_id:
            query = query.filter(Order.user_id == user_id)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def create_order(db: Session, order_data: OrderCreate) -> Order:
        """Create new order"""
        order = Order(**order_data.dict())
        db.add(order)
        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    def update_order(
        db: Session, order_id: int, order_data: OrderUpdate
    ) -> Optional[Order]:
        """Update order"""
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            return None

        update_data = order_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(order, key, value)

        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    def delete_order(db: Session, order_id: int) -> bool:
        """Delete order"""
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            return False

        db.delete(order)
        db.commit()
        return True
