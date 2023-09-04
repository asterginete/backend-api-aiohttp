import pytest

# Mock data for testing
mock_user_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "Test@1234"
}

# Tests for user routes

async def test_register_user(client):
    response = await client.post('/register', json=mock_user_data)
    assert response.status == 201
    data = await response.json()
    assert data['username'] == mock_user_data['username']

async def test_login_user(client):
    # First, register the user
    await client.post('/register', json=mock_user_data)

    # Now, login with the user's credentials
    response = await client.post('/login', json=mock_user_data)
    assert response.status == 200
    data = await response.json()
    assert 'token' in data

async def test_get_user(client):
    # First, register the user
    response = await client.post('/register', json=mock_user_data)
    data = await response.json()
    user_id = data['id']

    # Now, retrieve the user
    response = await client.get(f'/users/{user_id}/')
    assert response.status == 200
    data = await response.json()
    assert data['username'] == mock_user_data['username']

async def test_update_user(client):
    # First, register the user
    response = await client.post('/register', json=mock_user_data)
    data = await response.json()
    user_id = data['id']

    # Now, update the user's email
    updated_data = {
        "username": "testuser",
        "email": "updated@example.com",
        "password": "Test@1234"
    }
    response = await client.put(f'/users/{user_id}/', json=updated_data)
    assert response.status == 200
    data = await response.json()
    assert data['email'] == updated_data['email']

async def test_delete_user(client):
    # First, register the user
    response = await client.post('/register', json=mock_user_data)
    data = await response.json()
    user_id = data['id']

    # Now, delete the user
    response = await client.delete(f'/users/{user_id}/')
    assert response.status == 204

    # Ensure the user is deleted
    response = await client.get(f'/users/{user_id}/')
    assert response.status == 404
