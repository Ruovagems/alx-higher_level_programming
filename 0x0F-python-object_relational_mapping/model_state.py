#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class with the name and id attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    db_user = "your_mysql_username"
    db_password = "your_mysql_password"
    db_host = "your_mysql_host"
    db_name = "your_database_name"

    engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}/{db_name}")
    Base.metadata.create_all(engine)
