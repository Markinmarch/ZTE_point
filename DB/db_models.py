import sqlalchemy as sql
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
metadata = MetaData

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

    id = sql.Column(sql.Integer, primary_key = True)
    name = sql.Column(sql.String(length = 40), nullable = False)
    phone = sql.Column(sql.String, nullable = False)
    email = sql.Column(sql.String, mullable = False, unique = True)
    password = sql.Column(sql.String, nullable = False)

    def __str__(self):
        return '%s, %s, %s' % (self.id, self.name, self.email)
    
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
    
def create_table(engine):
    Base.metadata.create_all(engine)