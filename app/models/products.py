from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    
    # Relationships
    category = relationship('Category', back_populates='products')
    order_items = relationship('OrderItem', back_populates='product')
    ratings = relationship('Rating', back_populates='product')

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
