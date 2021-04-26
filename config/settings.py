from sqlalchemy import create_engine

class Settings:

    def __init__(self):
        self.engine = create_engine('sqlite:///database.db', echo=False)
