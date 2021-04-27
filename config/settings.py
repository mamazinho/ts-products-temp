from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

class Settings:

    Engine = create_engine('sqlite:///database.db', echo=False)
    Base = declarative_base()
