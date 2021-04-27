from config.database import Database
from models.product_model import ProductModel
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
            product = session.query(ProductModel).filter_by(id=self.product['id'])
            return product 

    def read_by_name(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(name=self.product['name'])
            return product 

    def read_by_gtin(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(gtin=self.product['gtin'])
            return product 
        
    def update(self):
        if not 'id' in self.product or not self.product['id']:
            return self.create()
        
        with Database() as session:
            the_product = session.query(ProductModel).filter_by(id=self.product['id'])
            the_product.update({
                'id': self.product['id'],
                'seller_id': self.product['seller_id'],
                'name': self.product['name'],
                'description': self.product['description'],
                'created_at': datetime.now(),
                'actual_stock': self.product['actual_stock'],
                'actual_price': self.product['actual_price'],
                'gtin': self.product['gtin'],
            })

            session.commit()

    def delete(self):
        with Database() as session:
            try:
                session.query(ProductModel).filter_by(id=self.product['id']).delete()
            except Exception as e:
                print('Error >> ', e)

            session.commit()
