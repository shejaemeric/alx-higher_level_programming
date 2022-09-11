#!/usr/bin/python3
"""database using alchemy"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base = declarative_base()
class State(Base):
    """state mapping class"""
    __tablename__ = 'states'

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String(128),nullable=False)
