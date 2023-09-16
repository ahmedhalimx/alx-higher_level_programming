#!/usr/bin/python3
"""
 a python file that contains the class definition of a State
 and an instance 'Base = declarative_base()'
 """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """
    A State Class with id and name attributes
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
