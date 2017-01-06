# Import settings

from sqlalchemy import Column, Integer, String
from data_storage.database import Base

import hashlib

# ----------------------------------
# Database Mapper
# ----------------------------------

class News(Base):
    """    Model Table News    """
    __tablename__ = 'news'

    # id, title, description, url, published_at,title_hash, time_stamp

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String)
    url = Column('url', String)
    url_hash = Column('url_hash', String)
    published_at = Column('published_at', String)
    time_stamp = Column('time_stamp', String)

    def __init__(self, title, description, url, url_hash, published_at, time_stamp):
        self.title = title
        self.description = description
        self.url = url
        self.url_hash = url_hash
        self.published_at = published_at
        self.time_stamp = time_stamp

    def __repr__(self):
        return '<Title %r>' % self.title
