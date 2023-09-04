import pytest
from app.models.items import Item
from app.models.users import User
from app.models.orders import Order
from app.models.products import Product
from app.models.categories import Category
from app.models.comments import Comment
from app.models.ratings import Rating

# Mock data for testing
mock_user_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "Test@1234"
}

mock_category_data = {
    "name": "Test Category"
}

mock_product_data = {
    "name": "Test Product",
    "category_id": 1,
    "price": 10.99
}

mock_order_data = {
    "user_id": 1,
    "product_ids": [1],
    "status": "pending"
}

mock_comment_data = {
    "user_id": 1,
    "content": "This is a test comment",
    "item_id": 1
}

mock_rating_data = {
    "user_id": 1,
    "rating": 5,
    "item_id": 1
}

# Tests for models

def test_create_user(session):
    user = User(**mock_user_data)
    session.add(user)
    session.commit()
    assert user.id is not None

def test_create_category(session):
    category = Category(**mock_category_data)
    session.add(category)
    session.commit()
    assert category.id is not None

def test_create_product(session):
    product = Product(**mock_product_data)
    session.add(product)
    session.commit()
    assert product.id is not None

def test_create_order(session):
    order = Order(**mock_order_data)
    session.add(order)
    session.commit()
    assert order.id is not None

def test_create_comment(session):
    comment = Comment(**mock_comment_data)
    session.add(comment)
    session.commit()
    assert comment.id is not None

def test_create_rating(session):
    rating = Rating(**mock_rating_data)
    session.add(rating)
    session.commit()
    assert rating.id is not None

