from controllers.product_controller import ProductController
from controllers.category_controller import CategoryController

from config.database import Database
from datetime import datetime

class Main:
    prod_create = {
        "name": "mais um produto",
        "description": "descricao",
        "seller_id": 1,
        "actual_stock": 20,
        "actual_price": 20,
        "gtin": "ASSAS",
        "active": True,
        "categories": []
    }
    prod_update = {
        "id": 1,
        "name": "altera produto",
        "description": "descricao",
        "seller_id": 1,
        "actual_stock": 20,
        "actual_price": 20,
        "gtin": "ASSAS",
        "active": True,
        "categories": []
    }
    prod_delete = {
        "id": 3,
    }

    def __init__(self):
        p = ProductController()
        c = CategoryController()
        # c.create_category('nova cat', 'essa é umanova cat')
        # p.create_product(
        #     name="Esse é um novo produto",
        #     description="novo prod",
        #     seller_id=1,
        #     actual_stock=20,
        #     actual_price=20,
        #     gtin="ASSAS",
        #     active=True,
        #     categories=[1]
        # )
        p.read_all_products()

Main()