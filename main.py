from models.product_model import ProductModel
from models.category_model import CategoryModel
from models.product_category_model import ProductCategoryModel
from models.product_price_model import ProductPriceModel
from models.product_stock_model import ProductStockModel
from daos.product_price_dao import ProductPriceDao
from daos.product_stock_dao import ProductStockDao
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController

# ProductModel()
from datetime import datetime
import time

class Main:

    def __init__(self):
        self.product_id = 1
        self.price_id = 1
        self.stock_id = 1
        self.categories = []
        self.seller_id = 99

        print('\nCriando Category')
        time.sleep(0)
        self.create_category()
        time.sleep(0)
        print('\nCriando Category')
        time.sleep(0)
        self.create_category()
        time.sleep(0)
        print('\nCriando Category')
        time.sleep(0)
        self.create_category()
        time.sleep(0)

        print('\nLendo Todos Categories')
        time.sleep(0)
        self.read_all_categories()
        time.sleep(0)
        print('\nAtualizando Category')
        time.sleep(0)
        self.update_category()
        time.sleep(0)
        print('\nLendo Todos Categories')
        time.sleep(0)
        self.read_all_categories()
        time.sleep(0)
        print('\nDeletendo Category:', self.categories[0])
        time.sleep(0)
        self.delete_category()
        time.sleep(0)

        print('\nCriando Product')
        time.sleep(0)
        self.create_product()
        time.sleep(0)
        print('\nLendo Todos Produtos')
        time.sleep(0)
        self.read_all_products()
        time.sleep(0)
        print('\nAtualizando Produto')
        time.sleep(0)
        self.update_product()
        time.sleep(0)
        print('\nLendo Produto por ID')
        time.sleep(0)
        self.read_product_by_id()
        time.sleep(0)
        print('\nAtualizando Preço')
        time.sleep(0)
        self.update_product_price()
        time.sleep(0)
        print('\nLendo Produto por Nome')
        time.sleep(0)
        self.read_product_by_name()
        time.sleep(0)
        print('\nAtualizando Estoque')
        time.sleep(0)
        self.update_product_stock()
        time.sleep(0)
        print('\nLendo Produto por GTIN')
        time.sleep(0)
        self.read_product_by_gtin()
        time.sleep(0)
        print('\nInativando Produto:', self.product_id)
        time.sleep(0)
        self.delete_category()
        time.sleep(0)
        print('\nLendo Produto por Seller')
        time.sleep(0)
        self.read_product_by_seller_id()
        time.sleep(0)

        
        

        print('\nCriando Product Price')
        time.sleep(0)
        self.create_product_price()
        time.sleep(0)
        print('\nLendo Todos Product Price')
        time.sleep(0)
        self.read_all_product_price()
        time.sleep(0)


        print('\nCriando Product Stock')
        time.sleep(0)
        self.create_product_stock()
        time.sleep(0)
        print('\nLendo Todos Product Stock')
        time.sleep(0)
        self.read_all_product_stock()
        time.sleep(0)



    def create_category(self):
        id = CategoryController().create_category('teste cat', 'teste desc')
        self.categories.append(id)
        print("Criado Category com id:", id)

    def read_all_categories(self):
        list_categories = CategoryController().read_all_categories()
        for cat in list_categories:
            print(cat)
        print("Categorias Lida")

    def delete_category(self):
        CategoryController().delete_category(self.categories[0])
        self.categories.pop(0)
        print("Categoria Deletada")

    def update_category(self):
        CategoryController().update_category(self.categories[0], 'teste cat update', 'teste cat desc update')            
        print("Categoria Atualizada")






    def create_product(self):
        id = ProductController().create_product('teste prod', 'teste desc', self.seller_id, 10, 10, 'teste gtin', True, self.categories)
        self.product_id = id
        print("Criado Produto com id:", id)

    def read_all_products(self):
        products = ProductController().read_all_products()
        for prod in products:
            print(prod)
    
    def update_product(self):
        ProductController().update_product(self.product_id, 'Test Prod', "Test prod desc", self.seller_id, 15, 15, 'test gtin updated', True, [self.categories[0]])
        print("Produto Atualizado")

    def update_product_price(self):
        ProductController().update_product(self.product_id, actual_price=5)
        print("Preço Atualizado")

    def update_product_stock(self):
        ProductController().update_product(self.product_id, actual_stock=10)
        print("Estoque Atualizado")

    def read_product_by_id(self):
        product = ProductController().read_by_id(self.product_id)
        print(product)
        print("Produto Lido")

    def read_product_by_name(self):
        product = ProductController().read_by_name('Test Prod')
        print(product)
        print("Produto Lido")

    def read_product_by_gtin(self):
        product = ProductController().read_by_gtin('test gtin updated')
        print(product)
        print("Produto Lido")

    def read_product_by_seller_id(self):
        product = ProductController().read_by_seller_id(self.seller_id)
        print(product)
        print("Produto Lido")

    def delete_product(self):
        product = ProductController().delete_product(self.seller_id)
        print(product)
        print("Produto Deletado")





    def create_product_price(self):
        id = ProductController().create_product_price(self.product_id, 10)
        self.price_id = id
        print("Criado Product Price com id:", id)

    def read_all_product_price(self):
        prices = ProductController().read_all_product_price()
        for price in prices:
            print(price)
        print('Product Price lido')






    def create_product_stock(self):
        id = ProductController().create_product_stock(self.product_id, 10)
        self.stock_id = id
        print("Criado Product Stock com id:", id)

    def read_all_product_stock(self):
        stocks = ProductController().read_all_product_stock()
        for stock in stocks:
            print(stock)
        print('Product Stock lido')



Main()