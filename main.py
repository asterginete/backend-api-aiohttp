from aiohttp import web
import asyncio
import json
import jwt
import bcrypt

# Mock databases (in-memory dictionaries)
items_db = {}
users_db = {}
orders_db = {}
products_db = {}
categories_db = {}
comments_db = {}

SECRET_KEY = "your_secret_key_here"  # This should be kept secret and stored securely

# Generic CRUD functions
async def create_resource(request, db):
    data = await request.json()
    resource_id = str(len(db) + 1)
    db[resource_id] = data
    return web.Response(text=json.dumps({"id": resource_id}), status=201)

async def get_resource(request, db):
    resource_id = request.match_info.get('id', None)
    if resource_id in db:
        return web.Response(text=json.dumps(db[resource_id]))
    return web.Response(status=404)

async def update_resource(request, db):
    resource_id = request.match_info.get('id', None)
    if resource_id not in db:
        return web.Response(status=404)
    data = await request.json()
    db[resource_id] = data
    return web.Response(text=json.dumps(db[resource_id]))

async def delete_resource(request, db):
    resource_id = request.match_info.get('id', None)
    if resource_id in db:
        del db[resource_id]
        return web.Response(status=204)
    return web.Response(status=404)

# Authentication and Authorization functions
async def register(request):
    data = await request.json()
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    if username in users_db:
        return web.Response(text=json.dumps({"error": "User already exists"}), status=400)

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users_db[username] = {
        'username': username,
        'password': hashed_password.decode('utf-8')
    }

    return web.Response(text=json.dumps({"message": "User registered successfully"}), status=201)

async def login(request):
    data = await request.json()
    username = data.get('username')
    password = data.get('password')

    user = users_db.get(username)

    if not user:
        return web.Response(text=json.dumps({"error": "Invalid credentials"}), status=401)

    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        # Generate JWT token
        token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
        return web.Response(text=json.dumps({"token": token}), status=200)
    else:
        return web.Response(text=json.dumps({"error": "Invalid credentials"}), status=401)

def jwt_middleware(app, handler):
    async def middleware(request):
        if request.path.startswith('/login') or request.path.startswith('/register'):
            return await handler(request)

        token = request.headers.get('Authorization')
        if not token:
            return web.Response(text=json.dumps({"error": "Token missing"}), status=401)

        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user = decoded_token.get('username')
        except jwt.ExpiredSignatureError:
            return web.Response(text=json.dumps({"error": "Token has expired"}), status=401)
        except jwt.InvalidTokenError:
            return web.Response(text=json.dumps({"error": "Invalid token"}), status=401)

        return await handler(request)
    return middleware

# Routes
app = web.Application(middlewares=[jwt_middleware])

# Authentication routes
app.router.add_post('/register', register)
app.router.add_post('/login', login)

# Items
app.router.add_post('/items/', lambda request: create_resource(request, items_db))
app.router.add_get('/items/{id}/', lambda request: get_resource(request, items_db))
app.router.add_put('/items/{id}/', lambda request: update_resource(request, items_db))
app.router.add_delete('/items/{id}/', lambda request: delete_resource(request, items_db))

# Users
app.router.add_post('/users/', lambda request: create_resource(request, users_db))
app.router.add_get('/users/{id}/', lambda request: get_resource(request, users_db))
app.router.add_put('/users/{id}/', lambda request: update_resource(request, users_db))
app.router.add_delete('/users/{id}/', lambda request: delete_resource(request, users_db))

# Orders
app.router.add_post('/orders/', lambda request: create_resource(request, orders_db))
app.router.add_get('/orders/{id}/', lambda request: get_resource(request, orders_db))
app.router.add_put('/orders/{id}/', lambda request: update_resource(request, orders_db))
app.router.add_delete('/orders/{id}/', lambda request: delete_resource(request, orders_db))

# Products
app.router.add_post('/products/', lambda request: create_resource(request, products_db))
app.router.add_get('/products/{id}/', lambda request: get_resource(request, products_db))
app.router.add_put('/products/{id}/', lambda request: update_resource(request, products_db))
app.router.add_delete('/products/{id}/', lambda request: delete_resource(request, products_db))

# Categories
app.router.add_post('/categories/', lambda request: create_resource(request, categories_db))
app.router.add_get('/categories/{id}/', lambda request: get_resource(request, categories_db))
app.router.add_put('/categories/{id}/', lambda request: update_resource(request, categories_db))
app.router.add_delete('/categories/{id}/', lambda request: delete_resource(request, categories_db))

# Comments
app.router.add_post('/comments/', lambda request: create_resource(request, comments_db))
app.router.add_get('/comments/{id}/', lambda request: get_resource(request, comments_db))
app.router.add_put('/comments/{id}/', lambda request: update_resource(request, comments_db))
app.router.add_delete('/comments/{id}/', lambda request: delete_resource(request, comments_db))

if __name__ == '__main__':
    web.run_app(app)
