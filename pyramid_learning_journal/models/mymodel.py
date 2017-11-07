import datetime

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


class Entries(Base):
    """Class for journal entries."""
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    creation_date = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return '<Entries: {}>'.format(self.title)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
