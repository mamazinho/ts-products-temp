from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.settings import Settings

class ProductCategoryModel(Settings.Base):

    __tablename__ = 'product_category'

    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    category_id  = Column(Integer, ForeignKey('category.id'), primary_key=True)