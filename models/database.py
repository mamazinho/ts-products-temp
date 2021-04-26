from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.base import Base
from config.settings import Settings


class Database:

    def __enter__(self):
        engine = create_engine('sqlite:///database.db', echo=True)
        Base.metadata.create_all(Settings().engine, checkfirst=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()