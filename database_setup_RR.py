import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Company(Base):
    __tablename__ = 'boardGameCompany'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

class BoardGame(Base):
    __tablename__ = 'boardGame'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    num_of_players = Column(String(30))
    play_time = Column(String(20))
    cost = Column(String(15))
    rating = Column(String(50))
    description = Column(String(300))
    company_id = Column(Integer, ForeignKey('boardGameCompany.id'))
    boardGameCompany = relationship(Company)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'num_of_players': self.num_of_players,
            'play_time': self.play_time,
            'cost': self.cost,
            'rating': self.rating,
            'company_id': self.company_id,
            'description': self.description,
        }


engine = create_engine('sqlite:///gamemenu.db')


Base.metadata.create_all(engine)
