#!/usr/bin/python3
"""Database storage"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
classes = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """Database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes database storage"""
        db_user = getenv('HBNB_MYSQL_USER')
        db_passwd = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
				      .format(db_user, db_passwd, db_host, db),
				      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dict of objs"""
        if not self.__session:
            self.reload()
        objs = {}
        if type(cls) == str:
            cls = classes.get(cls, None)
        if cls is not None:
            for obj in self.__session.query(cls):
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls):
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
        return objs

    def reload(self):
        """reloads objs"""
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(Session)

    def new(self, obj):
        """creates a new object"""
        self.__session.add(obj)

    def save(self):
        """saves the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an obj"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)
