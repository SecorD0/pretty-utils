import logging

import mysql.connector


class DBException(Exception):
    pass


class DB():
    def __init__(self, database="database", host="localhost", user="root", passwd=None, **kwargs):
        self.database = database
        if not self.database:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                passwd=passwd,
                autocommit=True
            )
        else:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=self.database,
                autocommit=True
            )
        try:
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise DBException(f'\n{str(e)}')

    def execute(self, query, data=None, ret1=False):
        try:
            if not self.conn:
                self.__init__(self.database)
            else:
                if data:
                    self.cursor.execute(query, data)
                else:
                    self.cursor.execute(query)

                if 'INSERT' in query or 'UPDATE' in query or 'DELETE' in query or 'DROP' in query:
                    self.conn.commit()

                elif 'SELECT' in query:
                    if ret1:
                        return self.cursor.fetchone()
                    else:
                        return self.cursor.fetchall()

        except Exception as e:
            logging.error('connection', exc_info=True)
            raise DBException(f'\n{str(e)}')
