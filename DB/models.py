from typing import Any
from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Boolean,
    or_,
    and_
    )
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
    
    id = Column(Integer, nullable = False, primary_key = True)
    name = Column(String(length = 40), nullable = False)
    phone = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    role = Column(String, default = 'user', nullable = False)
    
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
        user_role: str | Any
    ) -> None:
        with session:
            session.add(
                User(
                    name = user_name,
                    phone = user_phone,
                    email = user_email,
                    password = generate_password_hash(user_password),
                    role = user_role
                )
            )
            session.commit()
        
    def get_user(user_id: int) -> object:
        # связано со входом пользователя на сайт, исключительно служебный метод
        with session:
            return session.query(User).filter_by(id = user_id).first()
        
    def check_email(user_email: str) -> bool:
        # так как наши адреса почты уникальные (unique = True) и не может быть больше одного в БД,
        # мы можем по количеству == 1, определить, что запись имеется.
        with session:
            if session.query(User).filter_by(email = user_email).count() == True:
                return True
            return False

    def check_user(
        user_email: str,
        user_password: str
    ):
        with session:
            user = session.query(User).filter_by(email = user_email).first()
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
    
    def get_items() -> list:
        with session:
            return session.query(Item).all()
        
    def search_items(keywords: set) -> list:
        with session:
            for words in keywords:
                return session.query(Item).filter(or_(
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
    count = Column(Integer, default = 1, nullable = False)
    paid_status = Column(Boolean, default = False, nullable = False)
    
    user = relationship(User, backref = 'bascket')
    item = relationship(Item, backref = 'bascket')
    
    def add_items(
        user_id: int,
        item_id: int,
        item_count: int
    ) -> None:
        with session:
            check_item_in_bascket = session.query(Bascket).filter(and_(Bascket.id_user == user_id, Bascket.id_item == item_id, Bascket.paid_status == False))
            if check_item_in_bascket.count() == True:
                for count_item_in_bascket in check_item_in_bascket:
                    count_item_in_bascket.count += item_count
            else:
                session.add(
                    Bascket(
                        id_user = user_id,
                        id_item = item_id,
                        count = item_count
                    )
                )
            session.commit()
            
    def join_bascket_item(user_id: int) -> list:
        with session:
            inner_join_query = session.query(Bascket, Item).join(Bascket, Item.id == Bascket.id_item)
            return inner_join_query.filter(and_(Bascket.id_user == user_id, Bascket.paid_status == False)).all()       
         
    def not_paid_item_list(self, user_id: int) -> list:
        full_list = []
        for bascket, item in self.join_bascket_item(user_id):
            full_list.append({
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'unit': item.unit,
                'index': item.index,
                'parametrs': item.parametrs,
                'description': item.description,
                'image': item.image,
                'count': bascket.count,
                'paid_status': bascket.paid_status
            })
        return full_list
    
    def tatal_price(self, user_id: int):
        total = 0
        for bascket, item in self.join_bascket_item(user_id):
            amount_by_quantity = item.price * bascket.count
            total += amount_by_quantity
        return "{:.2f}".format(round(total, 2))
        
    def delete_item(
        user_id: int,
        item_id: int
    ) -> None:
        with session:
            item_to_delete = session.query(Bascket).filter(and_(Bascket.id_user == user_id, Bascket.id_item == item_id, Bascket.paid_status == False)).one()
            session.delete(item_to_delete)
            session.commit()
            
    def update_before_payment(
        user_id: int,
        item_id: int,
        item_count: int
    ) -> None:
        with session:
            session.query(Bascket).filter(and_(Bascket.id_user == user_id, Bascket.id_item == item_id, Bascket.paid_status == False)).update({'count': item_count})
            session.commit()
            
    def payment(user_id: int) -> None:
        with session:
            paid_items = session.query(Bascket).filter(and_(Bascket.id_user == user_id, Bascket.paid_status == False)).all()
            for paid_item in paid_items:
                paid_item.paid_status = True
            session.commit()
            
    def __str__(self):
        return '%s: %s, %s' % (self.id_user, self.id_item, self.count)

class Order(Base):
    __tablename__ = 'order'
    
    id = Column(Integer, primary_key = True, nullable = False)
    id_user = Column(Integer, ForeignKey('user.id'), nullable = False)
    date = Column(String, default = datetime.now().strftime("%d.%m.%Y --> %H:%M"))
    paid_status = Column(Boolean, nullable = False)
    
    user = relationship(User, backref = 'order')
    
    def item_list(user_id: int) -> list:
        with session:
            inner_join_query = session.query(Bascket, Item).join(Bascket, Item.id == Bascket.id_item)
            params_to_paid = inner_join_query.filter(and_(Bascket.id_user == user_id, Bascket.paid_status == True)).all()
            full_list = []
            for bascket, item in params_to_paid:
                full_list.append({'item_id': item.id, 'item_price': item.price, 'count': bascket.count, 'status': bascket.paid_status})
            return full_list.append(Order.id, Order.id_user, Order.paid_status)