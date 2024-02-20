import logging
from psycopg2 import connect, Error, errors
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from config import (
    postgres_database,
    postgres_host,
    postgres_password,
    postgres_port,
    postgres_user
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


# ---------------подключение к базе данных PostgreSQL----------------
DSN = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (postgres_user, postgres_password, postgres_host, postgres_port, postgres_database)

engine = create_engine(DSN)
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

class User(Base, UserMixin):
    '''
    Объект "User" - структура таблицы БД для пользователей.
        Параметры:
            id(int): идентефикатор пользователя;
            name(len(str) <= 40): имя пользователя;
            phone(str): номер телефона пользователя;
            email(str): адрес электронной почты;
            password(str): пароль от личного кабинета;
        Возвращаемое значение:
            str(id, name, email)
    '''
    __tablename__ = 'user'

    id = Column(Integer, nullable = False, primary_key = True)
    name = Column(String(length = 40), default = None, nullable = False)
    phone = Column(String, default = None, nullable = False)
    email = Column(String, default = None, nullable = False, unique = True)
    password = Column(String, default = None, nullable = False)

    def __str__(self):
        return '%s, %s, %s' % (self.id, self.name, self.email)
    
    def insert_user(
        # self,
        user_name: str,
        user_phone: str,
        user_email: str,
        user_password: str
    ) -> None:
        session.add(
            User(
                name = user_name,
                phone = user_phone,
                email = user_email,
                password = generate_password_hash(user_password)
        ))
        session.commit()
        session.close()
        
    def check_user(
        # self,
        user_email: str,
        user_password: str
    ):
        return session.query(User).filter(User.email == user_email)
    
class Item(Base):
    '''
    Объект "Item" - структура таблицы БД для товара, деталей.
        Параметры:
            id(int): иентификатор товара;
            name(len(str) <= 100): название товара;
            price(float): цена за еденицу товар;
            index(int): товарный индекс;
        Возвращаемое значение:
            str(id: name, price, index)
    '''
    __tablename__ = 'item'

    id = Column(Integer, primary_key = True)
    name = Column(String(length = 100), nullable = False)
    price = Column(Float, nullable = False)
    index = Column(Integer, nullable = True, unique = True)

    def __str__(self):
        return '%s: %s, %s, %s' % (self.id, self.name, self.price, self.index)

class Order(Base):
    '''
    Объект "Order" - структура таблицы БД для заказов польвателей.
        Параметры:
            id(int): идентификатор заказа;
            date(str): дата заказа;
            id_item(int): идентификатор товара;
            id_user(int): идентификатор пользователя;
        Возвращаемое значение:
            str(id: id_user, id_item)
    '''
    __tablename__ = 'order'

    id = Column(Integer, primary_key = True)
    date = Column(Date, nullable = False)
    id_item = Column(Integer, ForeignKey('item.id'), nullable = False)
    id_user = Column(Integer, ForeignKey('user.id'), nullable = False)

    user = relationship(User, backref = 'order')
    item = relationship(Item, backref = 'order')

    def __str__(self):
        return '%s: %s, %s' % (self.id, self.id_user, self.item)

def create_table(): 
    Base.metadata.create_all(engine)
#избавились от переменной (ссылки) tables за ненадобностью