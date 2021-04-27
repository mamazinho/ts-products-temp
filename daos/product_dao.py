from config.database import Database
from models.product_model import ProductModel
from models.category_model import CategoryModel
from datetime import datetime

class ProductDao:

    def __init__(self, product={}):
        self.product = product

    def create(self):
        with Database() as session:
            categories = self.__categories_object(session, self.product.get('categories'))
                
            product = ProductModel(
                seller_id = self.product['seller_id'],
                name = self.product['name'],
                description = self.product['description'],
                created_at = datetime.now(),
                actual_stock = self.product['actual_stock'],
                actual_price = self.product['actual_price'],
                gtin = self.product['gtin'],
                categories = categories
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
            product = session.query(ProductModel).filter_by(id=self.product['id']).all()
            return product[0]


    def read_by_name(self):
        with Database() as session:
            product = session.query(ProductModel).filter(ProductModel.name.contains(self.product['name'])).all()
            return product[0]

    def read_by_gtin(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(gtin=self.product['gtin'])
            return product[0] 

    def read_by_seller_id(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(seller_id=self.product['seller_id']).all()
            return product[0]

    def update(self):
        if not 'id' in self.product or not self.product['id']:
            return self.create()
        
        with Database() as session:
            categories = self.__categories_object(session, self.product.get('categories'))
            the_product = session.query(ProductModel).filter_by(id=self.product['id'])
            the_product.update({
                'id': self.product['id'],
                'seller_id': self.product['seller_id'] if self.product['seller_id'] else the_product[0].seller_id,
                'name': self.product['name'] if self.product['name'] else the_product[0].name,
                'description': self.product['description'] if self.product['description'] else the_product[0].description,
                'created_at': datetime.now(),
                'actual_stock': self.product['actual_stock'] if self.product['actual_stock'] else the_product[0].actual_stock,
                'actual_price': self.product['actual_price'] if self.product['actual_price'] else the_product[0].actual_price,
                'gtin': self.product['gtin'] if self.product['gtin'] else the_product[0].gtin,
            })
            the_product = session.query(ProductModel).get(self.product['id'])
            if categories:
                the_product.categories[:] = []
                for cat in categories:
                    the_product.categories.append(cat)
            session.commit()

    def __categories_object(self, session, product_categories):
        categories = []

        if product_categories:
            for category_id in product_categories:
                category = session.query(CategoryModel).filter_by(id=category_id)
                categories.append(category[0])
            
        return categories