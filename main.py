from aiohttp import web
import asyncio
import json

# Mock databases (in-memory dictionaries)
items_db = {}
users_db = {}
orders_db = {}
products_db = {}
categories_db = {}
comments_db = {}

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

# Routes
app = web.Application()

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
