from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class EntryContent(Base):
    __tablename__ = 'resources'
    id = Column(Integer,primary_key=True)
    title = Column(String(128))
    url = Column(Text)
    tag = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, url=None, tag=None, date=None):
        self.title = title
        self.url = url
        self.tag = tag
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)
