from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.base import Base

class CategoryModel(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)