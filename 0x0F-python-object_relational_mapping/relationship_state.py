#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class with the name and id attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", back_populates="state")

if __name__ == "__main__":
    # Modify your connection details
    db_user = "your_mysql_username"
    db_password = "your_mysql_password"
    db_host = "localhost"
    db_name = "hbtn_0e_100_usa"
    
    engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}/{db_name}")
    Base.metadata.create_all(engine)
