# import logging
from psycopg2 import connect, Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import (
    postgres_database,
    postgres_host,
    postgres_password,
    postgres_port,
    postgres_user
)

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
            port = self.port,
            # database = self.database
        )
        self.cursor = self.connection.cursor()
    
    def create_database(self) -> object:
        try:
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor.execute(query = 'CREATE DATABASE %s;' % (self.database, ))
        except (Error, Exception) as error:
           print(f'The database has not been created. Please check the status of postgres and try again.\n{error}')
        finally:
            self.cursor.close()
            self.connection.close()
            print('Success! Database is created')

    def session(self) -> None:
        try:
            dsn_params = self.connection.get_dsn_parameters()
            print(dsn_params)
            self.cursor.execute(query = 'SELECT version();')
            record = self.cursor.fetchone()
            print(record)
        except (Error, Exception) as error:
            print(error)
        finally:
            self.cursor.close()
            self.connection.close()
            print('Session is closed')

        # try:
        #     # Подключение к существующей базе данных
        #     connection = psycopg2.connect(user="postgres",
        #                                 # пароль, который указали при установке PostgreSQL
        #                                 password="1111",
        #                                 host="127.0.0.1",
        #                                 port="5432",
        #                                 database="postgres_db")

        #     # Курсор для выполнения операций с базой данных
        #     cursor = connection.cursor()
        #     # Распечатать сведения о PostgreSQL
        #     print("Информация о сервере PostgreSQL")
        #     print(connection.get_dsn_parameters(), "\n")
        #     # Выполнение SQL-запроса
        #     cursor.execute("SELECT version();")
        #     # Получить результат
        #     record = cursor.fetchone()
        #     print("Вы подключены к - ", record, "\n")

        # except (Exception, Error) as error:
        #     print("Ошибка при работе с PostgreSQL", error)
        # finally:
        #     if connection:
        #         cursor.close()
        #         connection.close()
        #         print("Соединение с PostgreSQL закрыто")
            
db = DataBase(
    user = postgres_user,
    password = postgres_password,
    host = postgres_host,
    port = postgres_port,
    database = postgres_database
)
create_db = db.create_database()
session = db.session()

callable(create_db)