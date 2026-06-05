"""Database Initialization"""
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.product import Product
from app.models.order import Order
from app.services.user_service import UserService
from app.utils.logger import get_logger

logger = get_logger(__name__)


def init_db(db: Session) -> None:
    """Initialize database with sample data

    Args:
        db: Database session
    """
    # Check if data already exists
    if db.query(User).first():
        logger.info("Database already initialized")
        return

    logger.info("Initializing database with sample data...")

    # Create sample users
    user1 = User(
        username="admin",
        email="admin@example.com",
        password=UserService.hash_password("admin123"),
        is_active=True,
    )
    user2 = User(
        username="john",
        email="john@example.com",
        password=UserService.hash_password("john123"),
        is_active=True,
    )

    db.add(user1)
    db.add(user2)
    db.commit()
    logger.info(f"Created {2} users")

    # Create sample products
    product1 = Product(
        name="Laptop",
        description="High performance laptop",
        price=999.99,
        stock=10,
    )
    product2 = Product(
        name="Mouse",
        description="Wireless mouse",
        price=29.99,
        stock=50,
    )

    db.add(product1)
    db.add(product2)
    db.commit()
    logger.info(f"Created {2} products")

    logger.info("Database initialization completed")
