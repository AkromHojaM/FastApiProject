from datetime import datetime
from sqlalchemy import MetaData,Column, Integer, String, Date,Boolean,ForeignKey,Float
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base()



class User(Base):
    __tablename__ = 'User'
    metadata = metadata
    id = Column(Integer, primary_key=True,autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String,unique=True)
    email = Column(String,unique=True)
    registered_data = Column(Date,default=datetime.utcnow)
    is_admin = Column(Boolean,default=False)



class Color(Base):
    __tablename__ = 'color'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    count = Column(Integer)
    price = Column(Float)
    joined_date = Column(Date)
    description = Column(String)
    color = Column(ForeignKey('color.id'))



#count
#price
#joined_date
#color
#description

