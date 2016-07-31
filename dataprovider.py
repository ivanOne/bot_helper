from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SentryMember(Base):
    __tablename__ = 'sentry_member'
    id = Column(Integer, primary_key=True)
    t_id = Column(Integer)


def create_db():
    engine = create_engine('sqlite:///bot.db', echo=True)
    Base.metadata.create_all(engine)


def get_connection():
    engine = create_engine('sqlite:///bot.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session