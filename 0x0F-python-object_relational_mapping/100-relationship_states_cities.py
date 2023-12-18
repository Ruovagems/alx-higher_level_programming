#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    import sys

    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Assign command line arguments to variables
    db_user, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(db_user, db_password, db_name))
Base.metadata.create_all(engine)

    # Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

    # Create the State "California" with the City "San Francisco"
california = State(name="California", cities=[City(name="San Francisco")])
session.add(california)
session.commit()

    # Close the session
session.close()
