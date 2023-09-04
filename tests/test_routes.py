import pytest
from aiohttp import FormData

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

# Tests for routes

async def test_register_route(client):
    response = await client.post('/register', json=mock_user_data)
    assert response.status == 201

async def test_login_route(client):
    response = await client.post('/login', json=mock_user_data)
    assert response.status == 200

async def test_create_category(client):
    response = await client.post('/categories/', json=mock_category_data)
    assert response.status == 201

async def test_create_product(client):
    response = await client.post('/products/', json=mock_product_data)
    assert response.status == 201

async def test_create_order(client):
    response = await client.post('/orders/', json=mock_order_data)
    assert response.status == 201

async def test_create_comment(client):
    response = await client.post('/comments/', json=mock_comment_data)
    assert response.status == 201

async def test_create_rating(client):
    response = await client.post('/ratings/', json=mock_rating_data)
    assert response.status == 201

# ... Add more route tests as needed ...

