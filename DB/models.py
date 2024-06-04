from sqlalchemy import Column, ForeignKey, Integer, String, Float, or_, and_, join
from sqlalchemy.orm import relationship

from datetime import datetime

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
    
    id = Column(Integer, nullable = False, primary_key = True)
    name = Column(String(length = 40), nullable = False)
    phone = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    role = Column(String, default = "user", nullable = False)
    
    def __str__(self):
        return '%s, %s, %s' % (self.id, self.name, self.email)
    
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return True
    
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
        with session as sess:
            sess.add(
                User(
                    name = user_name,
                    phone = user_phone,
                    email = user_email,
                    password = generate_password_hash(user_password),
                    role = user_role
                )
            )
            sess.commit()
        
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
        with session as sess:
            user = sess.query(User).filter_by(email = user_email).first()
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

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(length = 100), nullable = False)
    price = Column(Float, nullable = False)
    unit = Column(String, default = 'ед.', nullable = False)
    index = Column(Integer, nullable = False, unique = True)
    parametrs = Column(String(length = 240), nullable = True)
    description = Column(String(length = 240), nullable = True)
    image = Column(String, nullable = True)

    def __str__(self):
        return '%s: %s, %s, %s, %s, %s, %s' % (self.id, self.name, self.price, self.unit, self.index, self.parametrs, self.description)
    
    def get_items():
        with session as sess:
            return sess.query(Item).all()
        
    def search_items(keywords: set) -> list:
        with session as sess:
            for words in keywords:
                return sess.query(Item).filter(or_(
                    Item.name.ilike(f'%{words}%'),
                    Item.parametrs.ilike(f'%{words}%'),
                    Item.description.ilike(f'%{words}%')
                    ))

class Bascket(Base):
    '''
    Объект "Bascket" - структура таблицы БД для корзины польвателей.
        Параметры:
            # id(int): идентификатор заказа;
            # date(str): дата заказа;
            id_item(int): идентификатор товара;
            id_user(int): идентификатор пользователя;
        Возвращаемое значение:
            str(id: id_user, id_item)
    '''
    __tablename__ = 'bascket'

    id = Column(Integer, primary_key = True, nullable = False)
    id_user = Column(Integer, ForeignKey('user.id'), nullable = False)
    id_item = Column(Integer, ForeignKey('item.id'), nullable = False)
    count = Column(Integer, nullable = False)
    
    user = relationship(User, backref = 'bascket')
    item = relationship(Item, backref = 'bascket')
    
    def add_items(
        user_id: int,
        item_id: int,
        count: int
    ) -> None:
        with session as sess:
            sess.add(
                Bascket(
                    id_user = user_id,
                    id_item = item_id,
                    count = count
                )
            )
            sess.commit()
            
    def item_list(user_id: int) -> list:
        with session as sess:
            inner_join_query = sess.query(Bascket, Item).join(Bascket, Item.id == Bascket.id_item).filter(Bascket.id_user == user_id).all()
            for bascket, item in inner_join_query:
                return [item.id, item.price, bascket.count]

    def __str__(self):
        return '%s: %s, %s' % (self.id_user, self.id_item, self.count)
#избавились от переменной (ссылки) tables за ненадобностью

class Order(Base):
    __tablename__ = 'order'
    
    id = Column(Integer, primary_key = True)
    date = Column(String, default = datetime.now().strftime("%d.%m.%Y --> %H:%M"))
    item_list = Column(String, nullable = False)
    status = Column(String, default = "not paid", nullable = True)