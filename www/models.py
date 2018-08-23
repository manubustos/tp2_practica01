import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Samples(Base):
    __tablename__ = 'samples'
    id=Column(Integer, primary_key=True)
    temperature=Column('temperature', Integer)
    humidity=Column('humidity', Integer)
    pressure=Column('pressure', Integer)
    windspeed=Column('windspeed', Integer)

