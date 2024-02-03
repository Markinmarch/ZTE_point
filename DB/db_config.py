import logging
from psycopg2 import connect, Error, errors
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

            
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
    cursor = connection.cursor()
    try:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor.execute(query = 'CREATE DATABASE %s;' % (database, ))
        logging.info('<--- Success! Database %s is created --->' % (database))
    except errors.DuplicateDatabase:
        logging.info(f'<--- Database "{database}" is ready --->')
    except Error as error:
        logging.error(f'<--- {error} --->')
    finally:
        cursor.close()
        connection.close()