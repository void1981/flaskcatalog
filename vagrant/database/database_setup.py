import sys
from sqlalchemy import Column, ForeignKey, Interger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

base = declarative_base()


class Restaurant (Base):
    __tablename__ = 'restaurant'
    name = Column(
        string(80), nullable=False
    )
    id = Column(
        integer, primary_key=True
    )


class MenuItem (Base):
    __tablename__ = 'menu_item'


####### insert at end of file #######

engine = create_engine(
    'sqlite:///restaurantmenu.db')

base.metadata.create_all(engine)
