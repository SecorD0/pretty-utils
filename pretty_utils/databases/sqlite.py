import sqlite3


class DBException(Exception):
    pass


def dynamic_class(class_name: str, variables: list or tuple, values: list or tuple):
    class_dict = dict(zip(variables, values))
    class_format = f'{class_name}('
    for i in range(len(variables)):
        class_format += f'{variables[i]}={repr(values[i])}, '
    metaclass = type(class_name, (type,), {'__repr__': lambda cls: class_format[:-2] + ')'})
    return metaclass(class_name, (object,), class_dict)


def make_sql(query: str, data: tuple = None, ret1: bool = False, ret_class: bool = True,
             with_column_names: bool = False,
             dbf: str = 'database.db'):
    with sqlite3.connect(dbf) as db:
        try:
            cursor = db.cursor()
            if data:
                try:
                    cursor.execute(query, data)
                except Exception as e:
                    raise DBException(f'\n{str(e)}')
            else:
                try:
                    cursor.execute(query)
                except Exception as e:
                    raise DBException(f'\n{str(e)}')

            db.commit()
            response = []
            try:
                headers = tuple([description[0] for description in cursor.description])
            except:
                headers = ()
            if with_column_names:
                response.append(headers)

            if ret1:
                try:
                    if ret_class:
                        return dynamic_class('data', headers, cursor.fetchone())
                    else:
                        if with_column_names:
                            response.append(cursor.fetchone())
                        else:
                            response = cursor.fetchone()
                except:
                    pass
            else:
                if ret_class:
                    response = []
                    for row in cursor.fetchall():
                        response.append(dynamic_class('data', headers, row))
                else:
                    response += cursor.fetchall()
            return response

        except Exception as e:
            raise DBException(f'\n{str(e)}')


class DB():
    def __init__(self, database, **kwargs):
        self.database = database
        self.db = sqlite3.connect(f'{database}.db', isolation_level=None)
        try:
            self.cursor = self.db.cursor()
        except Exception as e:
            raise DBException(f'\n{str(e)}')

    def execute(self, query: str, data: tuple = None, ret1: bool = False, ret_class: bool = True,
                with_column_names: bool = False):
        while True:
            try:
                if data:
                    self.cursor.execute(query, data)
                else:
                    self.cursor.execute(query)

                response = []
                try:
                    headers = tuple([description[0] for description in self.cursor.description])
                except:
                    headers = ()

                if with_column_names:
                    response.append(headers)

                if ret1:
                    try:
                        if ret_class:
                            return dynamic_class('data', headers, self.cursor.fetchone())
                        else:
                            if with_column_names:
                                response.append(self.cursor.fetchone())
                            else:
                                response = self.cursor.fetchone()
                    except:
                        pass
                else:
                    if ret_class:
                        response = []
                        for row in self.cursor.fetchall():
                            response.append(dynamic_class('data', headers, row))
                    else:
                        response += self.cursor.fetchall()

                return response

            except sqlite3.ProgrammingError as e:
                if 'Cannot operate on a closed cursor' in str(e):
                    self.__init__(self.database)
                else:
                    raise DBException(f'\n{str(e)}')

            except Exception as e:
                raise DBException(f'\n{str(e)}')
