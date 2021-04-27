from models.product_model import ProductModel
from models.category_model import CategoryModel
from models.product_category_model import ProductCategoryModel
from models.product_price_model import ProductPriceModel
from models.product_stock_model import ProductStockModel
from config.database import Database
from daos.product_price_dao import ProductPriceDao
from daos.product_stock_dao import ProductStockDao
# ProductModel()
from datetime import datetime
import time

class Main:

    def __init__(self):
        print('Criando Product Price')
        time.sleep(4)
        self.create_product_price()
        time.sleep(4)
        print('Lendo Todos Product Price')
        self.read_all_product_price()
        time.sleep(4)
        print('Lendo Product Price por product_id')
        self.read_by_product_id_product_price()
        time.sleep(4)
        print('Lendo Product Price por id')
        self.read_by_id_product_price()
        time.sleep(4)


        print('Criando Product Stock')
        time.sleep(4)
        self.create_product_stock()
        time.sleep(4)
        print('Lendo Todos Product Stock')
        self.read_all_product_stock()
        time.sleep(4)
        print('Lendo Product Stock por product_id')
        self.read_by_product_id_product_price()
        time.sleep(4)
        print('Lendo Product Stock por id')
        self.read_by_id_product_price()
        time.sleep(4)


    def create_product_price(self):
        tdict = {
                "product_id": 2,
                "price": 10
                }
        id = ProductPriceDao(tdict).create()
        print("Criado Product Price com id:", id)

    def read_all_product_price(self):
        prices = ProductPriceDao().read_all()
        for price in prices:
            print(price)
        print('Product Price lido')

    def read_by_product_id_product_price(self):
        tdict = {
                "product_id": 2
                }
        prices = ProductPriceDao(tdict).read_by_product_id()
        for price in prices:
            print(price)
        print('Product Price lido')
    
    def read_by_id_product_price(self):
        tdict = {
                "id": 1
                }
        price = ProductPriceDao(tdict).read_by_id()
        print(price)
        print('Product Price lido')






    def create_product_stock(self):
        tdict = {
                "product_id": 2,
                "stock": 10
                }
        id = ProductStockDao(tdict).create()
        print("Criado Product Stock com id:", id)

    def read_all_product_stock(self):
        stocks = ProductStockDao().read_all()
        for stock in stocks:
            print(stock)
        print('Product Stock lido')

    def read_by_product_id_product_stock(self):
        tdict = {
                "product_id": 2
                }
        stocks = ProductStockDao(tdict).read_by_product_id()
        for stock in stocks:
            print(stock)
        print('Product Stock lido')

    
    def read_by_id_product_stock(self):
        tdict = {
                "id": 1
                }
        stock = ProductStockDao(tdict).read_by_id()
        print(stock)
        print('Product Stock lido')




Main()