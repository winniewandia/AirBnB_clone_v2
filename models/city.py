#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60),
	    	          ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False, primary_key=True)
        places = relationship("Place", backref='cities', cascade="all, delete-orphan")
    else:
        state_id = ''
        name = ''
