from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from DB.main_db import Base, session


# ----------------модели БД-------------------------
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
    
    def __init__(self):
        pass

    id = Column(Integer, nullable = False, primary_key = True)
    name = Column(String(length = 40), default = None, nullable = False)
    phone = Column(String, default = None, nullable = False)
    email = Column(String, default = None, nullable = False, unique = True)
    password = Column(String, default = None, nullable = False)
    role = Column(String, default = "user", nullable = False)
    
    def __str__(self):
        return '%s, %s, %s' % (self.id, self.name, self.email, self.role)
    
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id
    
    def is_admin(self):
        if self.role == 'admin':
            return True
        return False
       
    def insert_user(
        user_name: str,
        user_phone: str,
        user_email: str,
        user_password: str,
        user_role: str
    ) -> None:
        with session as add_user:
            add_user.add(
                User(
                    name = user_name,
                    phone = user_phone,
                    email = user_email,
                    password = generate_password_hash(user_password),
                    role = user_role
                )
            )
            add_user.commit()
        
    def get_user(user_id: int) -> object:
        # связано со входом пользователя на сайт, исключительно служебный метод
        with session as get_user:
            return get_user.query(User).filter_by(id = user_id).first()
        
    def check_email(user_email: str) -> bool:
        # так как наши адреса почты уникальные (unique = True) и не может быть больше одного в БД,
        # мы можем по количеству == 1, определить, что запись имеется.
        with session as bool_email:
            if bool_email.query(User).filter_by(email = user_email).count() == True:
                return True
            return False

    def check_user(
        user_email: str,
        user_password: str
    ):
        with session as auth_user:
            user = auth_user.query(User).filter_by(email = user_email).first()
            if check_password_hash(user.password, user_password) == True:
                return user
    
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
    image = Column(String, nullable = True)

    def __str__(self):
        return '%s: %s, %s, %s' % (self.id, self.name, self.price, self.index)
    
    def get_items():
        with session as get_item:
            return get_item.query(Item).all()

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
#избавились от переменной (ссылки) tables за ненадобностью