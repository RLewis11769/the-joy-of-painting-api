from sqlalchemy import Column, Integer, String
from engine.db import Base

class Episode(Base):
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, unique=True)
    date = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f'<Episode {self.title}>'
