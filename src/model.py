from sqlalchemy import Column, String,Text,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer,primary_key=True)
    symbol = Column(String(255),primary_key=True)
    title = Column(String(255))
    text = Column(Text)
    description = Column(Text)

    def __init__(self,id,symbol,title,text,description):
        self.id = id
        self.symbol = symbol
        self.title = title
        self.text = text
        self.description = description

class Stock(Base):
    __tablename__ = 'stock'

    symbol = Column(String(50),primary_key=True)
    name = Column(String(50))

    def __init__(self,symbol,name):
        self.symbol = symbol
        self.name = name

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/xueqiu')
DBSession = sessionmaker(bind=engine)