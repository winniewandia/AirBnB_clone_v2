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
        objs = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for result in query:
                key = "{}.{}".format(type(result).__name__, result.id)
                objs[key] = result
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls):
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
        return objs

    def reload(self):
        """reloads objs"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Sec = scoped_session(Session)
        self.__session = Sec()

    def new(self, obj):
        """creates a new object"""
        self.__session.add(obj)

    def save(self):
        """saves the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an obj"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """calls remove()
        """
        self.__session.close()
