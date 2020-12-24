from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from actions import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

Base = declarative_base()


class XmasPresents:
    """Handle to store christmas presents in the database."""

    def __init__(self, db_url=None):
        """
        Handle to store christmas presents in the database.

        Creates the connection with the database and create table if it does not exist

        :param db_url: database connection.
        """
        if db_url is None:
            db_url = "postgresql://{}:{}@{}:{}/{}".format(
                DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
            )

        self.engine = create_engine(db_url, echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session()
        Base.metadata.create_all(self.engine)

    def add_present(self, name: str, present: str) -> "XmasPresentsModel":
        """
        Store present of a person in the database.

        :param name: person name.
        :param present: present name.
        :raise TypeError: name and present must be str and have length > 0.
        :return: XmasPresentsModel with the stored object.
        """
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError("argument 'name' must be str and have a length > 0.")

        if not isinstance(present, str) or len(present) == 0:
            raise TypeError("argument 'present' must be str and have a length > 0.")

        present = XmasPresentsModel(name=name, present=present)
        self.session.add(present)
        self.session.commit()
        self.session.refresh(present)
        return present


class XmasPresentsModel(Base):
    """Model to store christas presents of a person."""

    __tablename__ = "xmas_presents"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(63), index=True)
    present = Column(String(63))
    created_at = Column(DateTime, default=datetime.now)
