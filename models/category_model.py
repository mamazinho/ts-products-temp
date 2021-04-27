from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.settings import Settings

class CategoryModel(Settings.Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, sql_autoincrement=True)
    name = Column(String)
    description = Column(String)