from sqlalchemy.ext.asyncio import AsyncSession
from app.config import get_db
from app.models.products import Product
import random

async def recommend_products(user_id, num_recommendations=5):
    """
    Recommend products for a given user.
    
    Args:
    - user_id (int): The ID of the user for whom recommendations are to be made.
    - num_recommendations (int): The number of products to recommend. Default is 5.

    Returns:
    - list: A list of recommended products.
    """
    async with AsyncSession(get_db()) as session:
        # Fetch all products from the database
        all_products = await session.query(Product).all()

        # Mock recommendation logic
        # In a real-world scenario, you'd use user behavior, purchase history, etc., to generate recommendations.
        # For demonstration purposes, we'll just randomly select products.
        recommended_products = random.sample(all_products, min(num_recommendations, len(all_products)))

    # Convert the product objects to dictionaries for serialization
    result = [{"id": product.id, "name": product.name, "description": product.description} for product in recommended_products]
    return result
