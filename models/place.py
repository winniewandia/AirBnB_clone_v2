#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata, Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False), Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False, primary_key=True)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref='place', cascade="all, delete")
        amenities = relationship("Amenity", secondary='place_amenity', viewonly=False, backref="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """attribute that returns list of Review instances"""
            values_review = models.storage.all("Review").values()
            list_review = []
            for review in values_review:
                if review.place_id == self.id:
                    list_review.append(review)
            return list_review

        @property
        def amenities(self):
            """attribute that returns list of Amenity instances"""
            values_amenity = models.storage.all("Amenity").values()
            list_amenity = []
            for amenity in values_amenity:
                if amenity.place_id == self.id:
                    if amenity.id in amenity_ids:
                        list_amenity.append(amenity)
            return list_amenity

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == Amenity:
                self.amenities_ids.append(obj.id)
