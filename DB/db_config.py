import logging
from sqlalchemy import create_engine
from psycopg2 import connect, Error, errors
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from db_models import create_table


class DataBase:
    '''
    Объект "DataBase" реализует создание базы данных
    PostgreSQL на стороне сервера при условии, что
    данной базы данных ещё не существует. В противном
    случае объект ничего не делает.
        Параметры:
            user(str): имя пользователя БД;
            password(str): пароль от БД для данного пользователя;
            host(str): хост ресурса;
            port(str): порт ресурса;
            database(str): название/имя БД;
    '''
    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        port: str,
        database: str
    ) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
        )
        self.cursor = self.connection.cursor()
    
    def create_database(self) -> None:
        '''
        Метод непосредственно создаёт базу данных с проверкой
        на ошибки.
        '''
        try:
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor.execute(query = 'CREATE DATABASE %s;' % (self.database, ))
            logging.info('<--- Success! Database %s is created --->' % (self.database))
        except errors.DuplicateDatabase:
            logging.info(f'<--- Database "{self.database}" is ready --->')
        except Error as error:
            logging.error(f'<--- {error} --->')
        finally:
            self.cursor.close()
            self.connection.close()
