#!/usr/bin/python3
"""fetch first state python"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping = True)

session = sessionmaker(bind=engine)
session = session()

state = session.query(State).limit(1)
print('{}: {}'.format(state[0].id, state[0].name))

