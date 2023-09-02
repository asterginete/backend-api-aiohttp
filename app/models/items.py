from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Relationships
    comments = relationship('Comment', back_populates='item')
    ratings = relationship('Rating', back_populates='item')
    user = relationship('User', back_populates='items')

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, price={self.price})>"
