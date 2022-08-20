from typing import List, Optional

from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import sessionmaker, Session


class DBException(Exception):
    pass


class DB:
    def __init__(self, db_url: str, **kwargs):
        self.db_url = db_url
        self.create_database()
        self.engine = create_engine(self.db_url, **kwargs)
        self.Base = None
        session = sessionmaker(bind=self.engine)
        self.s: Session = session()
        self.conn = self.engine.connect()

    def create_database(self):
        """
        Creates a database if it doesn't exist.
        """
        try:
            db_url = self.db_url.split('/')
            database = db_url[-1]
            db_url = '/'.join(db_url[0:-1])
            engine = create_engine(db_url)
            with engine.connect() as conn:
                conn.execute('COMMIT')
                conn.execute(f'CREATE DATABASE {database}')
        except:
            pass

    def create_tables(self, base):
        """
        Creates tables.

        :param base: a base class for declarative class definitions
        """
        self.Base = base
        self.Base.metadata.create_all(self.engine)

    def all(self, entities, *criterion) -> list:
        """
        Fetches all rows.

        :param entities: an ORM entity
        :param criterion: criterion for rows filtering
        :return list: the list of rows
        """
        if criterion:
            return self.s.query(entities).filter(*criterion).all()
        return self.s.query(entities).all()

    def one(self, entities, *criterion, from_the_end: bool = False):
        """
        Fetches one row.

        :param entities: an ORM entity
        :param criterion: criterion for rows filtering
        :param from_the_end: get the row from the end
        :return list: found row or None
        """
        all = self.all(entities, *criterion)
        if all:
            if from_the_end:
                return all[-1]
            return all[0]
        return None

    def execute(self, query, *args):
        """
        Executes SQL query.

        :param query: the query
        :param args: any additional arguments
        """
        result = self.conn.execute(query, *args)
        self.commit()
        return result

    def commit(self):
        """
        Commits changes.
        """
        try:
            self.s.commit()
        except DatabaseError:
            self.s.rollback()

    def insert(self, row: object or List[object]):
        """
        Inserts rows.

        :param row: an ORM entity or list of entities
        """
        if isinstance(row, list):
            self.s.add_all(row)
        elif isinstance(row, object):
            self.s.add(row)
        else:
            DBException('Wrong type!')
        self.commit()
