#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref='place',
                               cascade="all, delete-orphan")
        amenities = relationship(
            "Amenity", secondary='place_amenity',
            viewonly=False, back_populates="place_amenities")
    else:
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
            from models.amenity import Amenity
            values_amenity = models.storage.all(Amenity).values()
            list_amenity = []
            for amenity in values_amenity:
                # if amenity.place_id == self.id:
                if amenity.id in self.amenity_ids:
                    list_amenity.append(amenity)
            return list_amenity

        @amenities.setter
        def amenities(self, obj=None):
            from models.amenity import Amenity
            if type(obj) is Amenity:
                self.amenities_ids.append(obj.id)
