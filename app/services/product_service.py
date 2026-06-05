"""Product Service"""
from sqlalchemy.orm import Session
from typing import Optional, List

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    """Product business logic service"""

    @staticmethod
    def get_product(db: Session, product_id: int) -> Optional[Product]:
        """Get product by ID"""
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def get_products(
        db: Session, skip: int = 0, limit: int = 10, is_active: bool = True
    ) -> List[Product]:
        """Get products with pagination"""
        query = db.query(Product).filter(Product.is_active == is_active)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def create_product(db: Session, product_data: ProductCreate) -> Product:
        """Create new product"""
        product = Product(**product_data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def update_product(
        db: Session, product_id: int, product_data: ProductUpdate
    ) -> Optional[Product]:
        """Update product"""
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None

        update_data = product_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete_product(db: Session, product_id: int) -> bool:
        """Delete product (soft delete by marking inactive)"""
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return False

        product.is_active = False
        db.commit()
        return True
