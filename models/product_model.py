from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from models.product_category_model import ProductCategoryModel
from sqlalchemy.orm import relationship
from config.settings import Settings
from datetime import datetime

class ProductModel(Settings.Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now())
    actual_stock = Column(Integer)
    actual_price = Column(Float)
    gtin = Column(String)
    active = Column(Boolean, default=True)
    categories = relationship('CategoryModel', secondary=ProductCategoryModel.table, back_populates='products', lazy='subquery')

    def __str__(self):
        return f"{self.id} - {self.seller_id} - {self.name} - {self.description} - {self.created_at} - {self.updated_at} - {self.actual_stock} - {self.actual_price} - {self.gtin} - {self.active} - {self.categories}"