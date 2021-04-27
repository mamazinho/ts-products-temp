from models.product_model import ProductModel
from models.category_model import CategoryModel
from models.product_category_model import ProductCategoryModel
from models.product_price_model import ProductPriceModel
from models.product_stock_model import ProductStockModel
from daos.product_dao import ProductDao
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
        print(ProductDao().read())
        ProductDao(self.prod_create).create()
        ProductDao(self.prod_update).update()
        ProductDao(self.prod_delete).delete()

Main()