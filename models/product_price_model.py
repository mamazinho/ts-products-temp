from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.base import Base
from datetime import datetime

class ProductPriceModel(Base):

    __tablename__ = 'product_price'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now())