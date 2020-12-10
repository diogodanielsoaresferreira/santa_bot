from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from actions import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

Base = declarative_base()


class XmasPresents:

    def __init__(self):
        """
        Create the connection with the database and create table if it does not exist
        """
        db_url = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
        self.engine = create_engine(db_url, echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

    def add_present(self, name: str, present: str) -> 'XmasPresentsModel':
        present = XmasPresentsModel(name=name, present=present)
        self.session.add(present)
        self.session.commit()
        self.session.refresh(present)
        return present


class XmasPresentsModel(Base):
    __tablename__ = 'xmas_presents'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(63), index=True)
    present = Column(String(63))
    created_at = Column(DateTime, default=datetime.now)