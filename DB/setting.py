import logging
from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
from psycopg2 import connect, Error, errors
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# from models import create_table


class DataBase:
    
    def __init__(
        self,
        user,
        password,
        host,
        port,
        database
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
    
    def session(self) -> object:
        DSN = "postgresql://%s:%s@%s:%s/%s" % (self.user, self.password, self.host, self.port, self.database, )
        return create_engine(DSN)
