from config.database import Database
from models.product_model import ProductModel
from models.product_category_model import ProductCategoryModel
from datetime import datetime

class ProductDao:

    def __init__(self, product={}):
        self.product = product

    def create(self):
        with Database() as session:
            product = ProductModel(
                seller_id = self.product['seller_id'],
                name = self.product['name'],
                description = self.product['description'],
                created_at = datetime.now(),
                actual_stock = self.product['actual_stock'],
                actual_price = self.product['actual_price'],
                gtin = self.product['gtin'],
            )
            session.add(product)
            session.flush()
            session.commit()
            return product.id

    def read(self):
        with Database() as session:
            products = session.query(ProductModel).all()
            return products

    def read_by_id(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(id=self.product['id']).first()
            return product 

    def read_by_name(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(name=self.product['name'])
            return product 

    def read_by_gtin(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(gtin=self.product['gtin'])
            return product 

    def read_by_seller_id(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(seller_id=self.product['seller_id']).all()
            return product

    def update(self):
        if not 'id' in self.product or not self.product['id']:
            return self.create()
        
        with Database() as session:
            the_product = self.read_by_id()
            the_product.update({
                'id': self.product['id'],
                'seller_id': self.product.get('seller_id', the_product.seller_id),
                'name': self.product.get('name', the_product.name),
                'description': self.product.get('description', the_product.description),
                'created_at': datetime.now(),
                'actual_stock': self.product.get('actual_stock', the_product.actual_stock),
                'actual_price': self.product.get('actual_price', the_product.actual_price),
                'gtin': self.product.get('gtin', the_product.gtin),
            })

            session.commit()