from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from models.product_category_model import ProductCategoryModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.settings import Settings

class CategoryModel(Settings.Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    products = relationship('ProductModel', secondary=ProductCategoryModel.table, back_populates='categories', lazy='subquery')


    def __str__(self):
        return f'{self.id} - {self.name} - {self.description}'