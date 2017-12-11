from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DataBase():
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:funkey2012@\
        localhost:3306/banques')
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()


class User(declarative_base()):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
