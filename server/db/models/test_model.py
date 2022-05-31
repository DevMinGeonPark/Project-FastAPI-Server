# models/test_model.py

from pydoc import describe
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Test(Base):
    # __tablename__ = "testTable"
    # id = Column(Integer, primary_key=True, index=True)
    # title = Column(String)
    # description = Column(String)
    __tablename__ = "testTable"
    test = Column(String(length=20), primary_key=True, index=True)
    # description = Column(String)