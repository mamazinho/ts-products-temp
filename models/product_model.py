from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.base import Base
from datetime import datetime

class ProductModel(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now())
    actual_stock = Column(Integer)
    actual_price = Column(Float)
    gtin = Column(String)
    active = Column(Boolean)
    categories = relationship('CategoryModel', secondary='product_category')