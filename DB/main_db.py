import logging

from psycopg2 import connect, Error, errors
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DATABASE
)

#-------------------Создание базы данных PostgreSQL-------------------
def create_database(
    user: str,
    password: str,
    host: str,
    port: str,
    database: str
):
    '''
    Метод "create_database" реализует создание базы данных
    PostgreSQL на стороне сервера при условии, что
    данной базы данных ещё не существует. В противном
    случае метод ничего не делает.
        Параметры:
            user(str): имя пользователя БД;
            password(str): пароль от БД для данного пользователя;
            host(str): хост ресурса;
            port(str): порт ресурса;
            database(str): название/имя БД;
    '''
    connection = connect(
        user = user,
        password = password,
        host = host,
        port = port
        )
    with connection.cursor() as cursor:
        try:
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor.execute(query = 'CREATE DATABASE %s;' % (database, ))
            logging.info('<--- Success! Database %s is created --->' % (database))
        except errors.DuplicateDatabase:
            logging.info(f'<--- Database "{database}" is ready --->')
        except Error as error:
            logging.error(f'<--- {error} --->')

# ---------------подключение к базе данных PostgreSQL----------------
DSN = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DATABASE)
engine = create_engine(DSN)
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

database = create_database(
    user = POSTGRES_USER,
    password = POSTGRES_PASSWORD,
    host = POSTGRES_HOST,
    port = POSTGRES_PORT,
    database = POSTGRES_DATABASE
)

def create_table(): 
    Base.metadata.create_all(engine)