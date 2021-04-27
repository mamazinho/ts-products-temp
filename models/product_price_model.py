from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.settings import Settings
from datetime import datetime

class ProductPriceModel(Settings.Base):

    __tablename__ = 'product_price'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now())

    def __str__(self):
        return f"{self.id} - {self.product_id} - {self.price} - {self.created_at}"