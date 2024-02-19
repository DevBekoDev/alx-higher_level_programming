#!/usr/bin/python3
""" ORM is powerful"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    update_state = session.query(State).filter(State.id == 2).all()
    if update_state:
        update_state[0].name = "New Mexico"
    session.commit()
    session.close()
