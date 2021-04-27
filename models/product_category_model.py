from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.settings import Settings

class ProductCategoryModel:

    table = Table(
        'product_category', 
        Settings.Base.metadata,
        Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
        Column('category_id', Integer, ForeignKey('category.id'), primary_key=True)
    )