from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_
from app.config import get_db
from app.models.products import Product

async def search_products(query):
    """
    Search products based on the given query.
    """
    async with AsyncSession(get_db()) as session:
        # Use the `ilike` function for case-insensitive search
        products = await session.query(Product).filter(
            or_(
                Product.name.ilike(f"%{query}%"),
                Product.description.ilike(f"%{query}%")
            )
        ).all()

    # Convert the product objects to dictionaries for serialization
    result = [{"id": product.id, "name": product.name, "description": product.description} for product in products]
    return result
