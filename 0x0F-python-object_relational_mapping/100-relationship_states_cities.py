#!/usr/bin/python3
# Creates the State "California" with the City "San Francisco"
# from the database hbtn_0e_100_usa.
# Usage: ./100-relationship_states_cities.py <mysql username> /
#                                            <mysql password> /
#                                            <database name>

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California", cities=[City(name="San Francisco")])
    session.add(california)
    session.commit()

    print("State and City added successfully.")
