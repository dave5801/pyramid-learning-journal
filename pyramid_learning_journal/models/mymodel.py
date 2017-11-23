"""Data Model."""


import datetime

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class Entries(Base):
    """Class for journal entries."""
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    creation_date = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
       return '<Entries: {}>'.format(self.title)
    
    def to_dict(self):
        """Take all model attributes and render them as a dictionary."""
        return {'id': self.id,
                'title': self.title,
                'body': self.body,
                'creation_date': self.creation_date.strftime('%A, %d %B, %Y, %I:%M %p')
                }
