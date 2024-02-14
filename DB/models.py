import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship
from werkzeug.security import generate_password_hash, check_password_hash

from . import engine, session


Base = declarative_base()

class User(Base):
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

    id = sql.Column(sql.Integer, nullable = False, primary_key = True)
    name = sql.Column(sql.String(length = 40), default = None, nullable = False)
    phone = sql.Column(sql.String, default = None, nullable = False)
    email = sql.Column(sql.String, default = None, nullable = False, unique = True)
    password = sql.Column(sql.String, default = None, nullable = False)

    def __str__(self):
        return '%s, %s, %s' % (self.id, self.name, self.email)
    
    def insert_user(
        self,
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
        self,
        user_email: int,
        user_password: str
    ) -> bool:
        return session.query(User).filter(User.email == user_email), check_password_hash(hash, user_password)
    
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

    id = sql.Column(sql.Integer, primary_key = True)
    name = sql.Column(sql.String(length = 100), nullable = False)
    price = sql.Column(sql.Float, nullable = False)
    index = sql.Column(sql.Integer, nullable = True, unique = True)

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

    id = sql.Column(sql.Integer, primary_key = True)
    date = sql.Column(sql.Date, nullable = False)
    id_item = sql.Column(sql.Integer, sql.ForeignKey('item.id'), nullable = False)
    id_user = sql.Column(sql.Integer, sql.ForeignKey('user.id'), nullable = False)

    user = relationship(User, backref = 'order')
    item = relationship(Item, backref = 'order')

    def __str__(self):
        return '%s: %s, %s' % (self.id, self.id_user, self.item)

def create_table(): 
    Base.metadata.create_all(engine)
#избавились от переменной (ссылки) tables за ненадобностью