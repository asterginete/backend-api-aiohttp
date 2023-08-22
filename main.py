from aiohttp import web
import asyncio
import json
import jwt
import bcrypt

# Mock databases (in-memory dictionaries)
resources = {
    "items": {},
    "users": {},
    "orders": {},
    "products": {},
    "categories": {},
    "comments": {}
}

SECRET_KEY = "your_secret_key_here"  # This should be kept secret and stored securely

# Schemas for basic validation
schemas = {
    "items": {"name", "description", "price"},
    "users": {"username", "email", "password"},
    "orders": {"user_id", "product_ids", "status"},
    "products": {"name", "category_id", "price"},
    "categories": {"name"},
    "comments": {"user_id", "content", "item_id"}
}

def validate_data(data, schema):
    """Validate data against a given schema."""
    return set(data.keys()) == schema

async def create_resource(request, resource_name):
    data = await request.json()
    
    # Validate input data
    if not validate_data(data, schemas[resource_name]):
        return web.Response(text="Invalid data format", status=400)
    
    resource_id = str(len(resources[resource_name]) + 1)
    resources[resource_name][resource_id] = data
    return web.Response(text=json.dumps({"id": resource_id}), status=201)

async def get_resource(request, resource_name):
    resource_id = request.match_info.get('id', None)
    if resource_id in resources[resource_name]:
        return web.Response(text=json.dumps(resources[resource_name][resource_id]))
    return web.Response(status=404)

async def update_resource(request, resource_name):
    resource_id = request.match_info.get('id', None)
    if resource_id not in resources[resource_name]:
        return web.Response(status=404)
    
    data = await request.json()
    
    # Validate input data
    if not validate_data(data, schemas[resource_name]):
        return web.Response(text="Invalid data format", status=400)
    
    resources[resource_name][resource_id] = data
    return web.Response(text=json.dumps(resources[resource_name][resource_id]))

async def delete_resource(request, resource_name):
    resource_id = request.match_info.get('id', None)
    if resource_id in resources[resource_name]:
        del resources[resource_name][resource_id]
        return web.Response(status=204)
    return web.Response(status=404)

# Authentication and Authorization functions
async def register(request):
    data = await request.json()
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    if username in resources.users:
        return web.Response(text=json.dumps({"error": "User already exists"}), status=400)

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    resources.users[username] = {
        'username': username,
        'password': hashed_password.decode('utf-8')
    }

    return web.Response(text=json.dumps({"message": "User registered successfully"}), status=201)

async def login(request):
    data = await request.json()
    username = data.get('username')
    password = data.get('password')

    user = resources.users.get(username)

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

for resource_name in resources.keys():
    app.router.add_post(f'/{resource_name}/', lambda request, resource=resource_name: create_resource(request, resource))
    app.router.add_get(f'/{resource_name}/{{id}}/', lambda request, resource=resource_name: get_resource(request, resource))
    app.router.add_put(f'/{resource_name}/{{id}}/', lambda request, resource=resource_name: update_resource(request, resource))
    app.router.add_delete(f'/{resource_name}/{{id}}/', lambda request, resource=resource_name: delete_resource(request, resource))

if __name__ == '__main__':
    web.run_app(app)
