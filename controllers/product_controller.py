from daos.product_dao import ProductDao
from daos.product_price_dao import ProductPriceDao
from daos.product_stock_dao import ProductStockDao


class ProductController:

    def __init__(self):
        pass

    # Products (this functions will be called by external APIs in the future)
    def create_product(self, name, description, seller_id, actual_stock, actual_price, gtin, active, categories=[]):
        product = {
            'name': name,
            'description': description,
            'seller_id': seller_id,
            'actual_stock': actual_stock,
            'actual_price': actual_price,
            'gtin': gtin,
            'active': active,
            'categories': categories,
        }
        product_id = ProductDao(product).create()
        self.create_product_price(product_id, actual_price)
        self.create_product_stock(product_id, actual_stock)
        return product_id

    def update_product(self, product_id, name=None, description=None, seller_id=None, actual_stock=None, actual_price=None, gtin=None, active=True, categories=[]):

        product = {
            'id': product_id,
            'name': name,
            'description': description,
            'seller_id': seller_id,
            'actual_stock': actual_stock,
            'actual_price': actual_price,
            'gtin': gtin,
            'active': active,
            'categories': categories,
        }
        ProductDao(product).update()

        if actual_price:
            self.create_product_price(product_id, actual_price)
        if actual_stock:
            self.create_product_stock(product_id, actual_stock)

    def delete_product(self, product_id):
        product = {
            'id': product_id,
            'active': False
        }
        ProductDao(product).update()

    def read_all_products(self):
        products = ProductDao().read()
        return products
    
    def read_by_id(self, product_id):
        product = {
            'id': product_id
        }
        products = ProductDao(product).read_by_id()
        return products

    def read_by_name(self, product_name):
        product = {
            'name': product_name
        }
        products = ProductDao(product).read_by_name()
        return products

    def read_by_gtin(self, product_gtin):
        product = {
            'gtin': product_gtin
        }
        products = ProductDao(product).read_by_gtin()
        return products

    def read_by_seller_id(self, product_seller_id):
        product = {
            'seller_id': product_seller_id
        }
        products = ProductDao(product).read_by_seller_id()
        return products


    # Product Price table (history of prices)
    def create_product_price(self, product_id, price):
        tdict = {
                "product_id": product_id,
                "price": price
                }
        id = ProductPriceDao(tdict).create()
        return id

    def read_all_product_price(self):
        prices = ProductPriceDao().read_all()
        return prices


    # Product Stock table (history of stocks)
    def create_product_stock(self, product_id, stock):
        tdict = {
                "product_id": product_id,
                "stock": stock
                }
        id = ProductStockDao(tdict).create()
        return id

    def read_all_product_stock(self):
        stocks = ProductStockDao().read_all()
        return stocks


# Examples of values
# prod_create = {
#     "name": "mais um produto",
#     "description": "descricao",
#     "seller_id": 1,
#     "actual_stock": 20,
#     "actual_price": 20,
#     "gtin": "ASSAS",
#     "active": True,
#     "categories": []
# }
# prod_update = {
#     "id": 1,
#     "name": "altera produto",
#     "description": "descricao",
#     "seller_id": 1,
#     "actual_stock": 20,
#     "actual_price": 20,
#     "gtin": "ASSAS",
#     "active": True,
#     "categories": []
# }
# prod_delete = {
#     "id": 3,
# }