#!/usr/bin/python3
"""Module that contains the class definition of City and instance Base"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class that inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")

# Add necessary import
from sqlalchemy.orm import relationship
