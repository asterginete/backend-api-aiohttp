from .views import items, users, orders, products, categories, comments, ratings

def setup_routes(app):
    # Authentication routes
    app.router.add_post('/register', users.register)
    app.router.add_post('/login', users.login)

    # Items routes
    app.router.add_post('/items/', items.create_item)
    app.router.add_get('/items/{id}/', items.get_item)
    app.router.add_put('/items/{id}/', items.update_item)
    app.router.add_delete('/items/{id}/', items.delete_item)

    # Users routes
    app.router.add_get('/users/{id}/', users.get_user)
    app.router.add_put('/users/{id}/', users.update_user)
    app.router.add_delete('/users/{id}/', users.delete_user)

    # Orders routes
    app.router.add_post('/orders/', orders.create_order)
    app.router.add_get('/orders/{id}/', orders.get_order)
    app.router.add_put('/orders/{id}/', orders.update_order)
    app.router.add_delete('/orders/{id}/', orders.delete_order)

    # Products routes
    app.router.add_post('/products/', products.create_product)
    app.router.add_get('/products/{id}/', products.get_product)
    app.router.add_put('/products/{id}/', products.update_product)
    app.router.add_delete('/products/{id}/', products.delete_product)

    # Categories routes
    app.router.add_post('/categories/', categories.create_category)
    app.router.add_get('/categories/{id}/', categories.get_category)
    app.router.add_put('/categories/{id}/', categories.update_category)
    app.router.add_delete('/categories/{id}/', categories.delete_category)

    # Comments routes
    app.router.add_post('/comments/', comments.create_comment)
    app.router.add_get('/comments/{id}/', comments.get_comment)
    app.router.add_put('/comments/{id}/', comments.update_comment)
    app.router.add_delete('/comments/{id}/', comments.delete_comment)

    # Ratings routes
    app.router.add_post('/ratings/', ratings.create_rating)
    app.router.add_get('/ratings/{id}/', ratings.get_rating)
    app.router.add_put('/ratings/{id}/', ratings.update_rating)
    app.router.add_delete('/ratings/{id}/', ratings.delete_rating)
