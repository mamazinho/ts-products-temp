from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.base import Base
from datetime import datetime

class ProductStockModel(Base):

    __tablename__ = 'product_stock'

    id = Column(Integer, primary_key=True, sql_autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    stock = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())