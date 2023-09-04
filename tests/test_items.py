import pytest

# Mock data for testing
mock_item_data = {
    "name": "Test Item",
    "description": "This is a test item",
    "price": 10.99
}

# Tests for item routes

async def test_create_item(client):
    response = await client.post('/items/', json=mock_item_data)
    assert response.status == 201
    data = await response.json()
    assert data['name'] == mock_item_data['name']

async def test_get_item(client):
    # First, create an item
    response = await client.post('/items/', json=mock_item_data)
    data = await response.json()
    item_id = data['id']

    # Now, retrieve the item
    response = await client.get(f'/items/{item_id}/')
    assert response.status == 200
    data = await response.json()
    assert data['name'] == mock_item_data['name']

async def test_update_item(client):
    # First, create an item
    response = await client.post('/items/', json=mock_item_data)
    data = await response.json()
    item_id = data['id']

    # Now, update the item
    updated_data = {
        "name": "Updated Item",
        "description": "This is an updated test item",
        "price": 15.99
    }
    response = await client.put(f'/items/{item_id}/', json=updated_data)
    assert response.status == 200
    data = await response.json()
    assert data['name'] == updated_data['name']

async def test_delete_item(client):
    # First, create an item
    response = await client.post('/items/', json=mock_item_data)
    data = await response.json()
    item_id = data['id']

    # Now, delete the item
    response = await client.delete(f'/items/{item_id}/')
    assert response.status == 204

    # Ensure the item is deleted
    response = await client.get(f'/items/{item_id}/')
    assert response.status == 404
