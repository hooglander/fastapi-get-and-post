from sqlalchemy import Column, Integer
from .database import Base


class Score(Base):
    __tablename__ = "score"

    id = Column(Integer, primary_key=True, index=True)
    home = Column(Integer)
    away = Column(Integer)
