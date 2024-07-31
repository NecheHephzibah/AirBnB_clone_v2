#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


<<<<<<< HEAD
class State(BaseModel):
    """ State class """
    name = ""
=======
class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                            backref="state")

    @property
    def cities(self):
        """Getter method for cities
        Returns the list of City objects linked to the current State
        """
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
>>>>>>> f10c55ce1b1b78ff7518aaa0beb07a7450ae3bc5
