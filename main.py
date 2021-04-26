from models.product_model import ProductModel
from models.category_model import CategoryModel
from models.product_category_model import ProductCategoryModel
from models.product_price_model import ProductPriceModel
from models.product_stock_model import ProductStockModel
from models.database import Database
# ProductModel()
from datetime import datetime

class Main:

    def __init__(self):
        ProductModel()
        with Database() as session:
            session.add(ProductModel(
                id=2,
                seller_id=1,
                name='test',
                description='test',
                created_at = datetime.now(),
                actual_stock = 20,
                actual_price = 10,
                gtin = 'ASDAS',
                active = True,
            ))

            session.commit()

Main()