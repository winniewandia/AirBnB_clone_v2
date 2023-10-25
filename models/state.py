#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade="all, delete")

    @property
    def cities(self):
        """getter attribute that returns City instances"""
        values_city = models.storage.all()
        list_city = []
        list_val = []
        for key in values_city:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_val.append(values_city[key])
        for value in list_val:
            if (value.state_id == self.id):
                list_city.append(value)
        return list_city
