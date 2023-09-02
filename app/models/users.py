from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
import bcrypt

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    
    # Relationships
    items = relationship('Item', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    ratings = relationship('Rating', back_populates='user')
    orders = relationship('Order', back_populates='user')
    socials = relationship('UserSocial', back_populates='user')

    def set_password(self, raw_password: str):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, raw_password: str) -> bool:
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
