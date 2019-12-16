#!/usr/bin/python3
"""
creates a city with sqlalchemy relationships
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                   .format(sys.argv[1], sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)

            Base.metadata.create_all(engine)

            Session = sessionmaker(bind=engine)
            session = Session()

            state = State("California")
            city = City("San Francisco")
            state.cities.append(city)
            session.add(city)
        except:
            print("something wrong about the query")

        finally:
            session.close()
