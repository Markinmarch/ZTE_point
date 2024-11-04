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
    and_,
    cast
    )
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship, column_property
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from DB.main_db import Base, session
from config import MAIN_URL

# ----------------модели БД-------------------------
class User(Base, UserMixin):
    '''
    Объект ``User`` - структура таблицы БД для пользователей.
    Вносит данные новых пользователей, проверяет и получает
    данные пользователей.
    '''
    __tablename__ = 'user'
    
    id = Column(Integer, nullable = False, primary_key = True)
    name = Column(String(length = 40), nullable = False)
    phone = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    role = Column(String, default = 'user', nullable = False)
    
    def __str__(self):
        '''
        Метод возвращает параметры пользователя.
            Return values:
                str(id, name, email);
        '''
        return '%s, %s, %s' % (self.id, self.name, self.email)
    
    def is_active(self):
        '''
        Метод возвращает состояние активности пользователя на сайте.
            Return values:
                bool;
        '''
        return True
    
    def is_authenticated(self):
        '''
        Метод возвращает состояние авторизованности пользователя на сайте.
            Return values:
                bool;
        '''
        return True
    
    def is_anonymous(self):
        '''
        Метод возвращает состояние анонимности пользователя на сайте.
            Return values:
                bool;
        '''
        return True
    
    def get_id(self):
        '''
        Метод возвращает идентификатор пользователя.
            Return values:
                id(int);
        '''
        return self.id
    
    def is_admin(self):
        '''
        Метод проверяет роль пользователя.
            Return values:
                bool;
        '''
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
        '''
        Метод вносит в базу данных параметры нового пользователя.
            Parametrs:
                id(int): идентефикатор пользователя;
                name(len(str) <= 40): имя пользователя;
                phone(str): номер телефона пользователя;
                email(str): адрес электронной почты;
                password(str): пароль от личного кабинета;
                role(str): роль пользователя в системе;
            Return values:
                None;
        '''
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
        '''
        Метод (служебный) реализует получение данных пользователя по указаным параметрам.
            Parametrs:
                user_id(int): идентефикатор пользователя;
            Return values:
                str(id, name, email);
        '''
        with session:
            return session.query(User).filter_by(id = user_id).first()
        
    def check_email(user_email: str) -> bool:
        '''
        Метод (служебный), определяет уникальность адреса регистрирующегося пользователя.
            Parametrs:
                user_email(str): адрес пользователя;
            Return values:
                bool;
          `# так как наши адреса почты уникальные (unique = True) и не может быть больше одного в БД,`
          `# мы можем по количеству == 1, определить, что запись имеется.`
        '''
        with session:
            if session.query(User).filter_by(email = user_email).count() == True:
                return True
            return False

    def check_user(
        user_email: str,
        user_password: str
    ) -> object|None:
        '''
        Метод (служебный) по параметрам адреса и пароля пользователя предоставляет данные
        для дальнейшей работы.
            Parametrs:
                user_email(str): адрес пользователя;
                user_password(str): пароль пользователя;
            Return values:
                object|None;
        '''
        with session:
            user = session.query(User).filter_by(email = user_email).first()
            if check_password_hash(user.password, user_password) == True:
                return user
    
class Item(Base):
    '''
    Объект ``Item`` - структура таблицы БД для товара, деталей.
        Parametrs:
            :param id: ``(int)`` иентификатор товара;
            :param name: ``(len(str) <= 100)`` название товара;
            :param price: ``(float)`` цена за еденицу товар;
            :param unit: ``(str)`` единица измерения;
            :param index: ``(int)`` товарный индекс;
            :param parametrs: ``(len(str) <= 240)`` параметры товара;
            :param description: ``(len(str) <= 240)`` описание товара;
            :param image: ``(str)`` внутренняя ссылка на изображение товара;
        Return values:
            str(id: name, price, unit, index, parametrs, description)
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
        return '%s: %s, %s, %s, %s, %s, %s, %s' % (
            self.id,
            self.name,
            self.price,
            self.unit,
            self.index,
            self.parametrs,
            self.description
        )
    
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
            id(int): идентификатор заказа;
            date(str): дата заказа;
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
    
    def __str__(self):
        return '%s: %s, %s, %s, %s' % (
            self.id,
            self.id_user,
            self.id_item,
            self.count,
            self.paid_status
        )
    
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
                    count_item_in_bascket.count += int(item_count)
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
            return session.query(Bascket, Item).join(Bascket, Item.id == Bascket.id_item)
         
    def not_paid_item_list(user_id: int) -> list:
        full_list = []
        for bascket, item in Bascket.join_bascket_item(user_id).filter(and_(Bascket.id_user == user_id, Bascket.paid_status == False)).all():
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
    
    def total_price(self, user_id: int) -> float:
        total = 0
        not_paid_total = self.join_bascket_item(user_id).filter(and_(Bascket.id_user == user_id, Bascket.paid_status == False)).all()
        for bascket, item in not_paid_total:
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
            ids_list = []
            for paid_item in paid_items:
                paid_item.paid_status = True
                ids_list.append(paid_item.id)
            session.add(Order(id_user = user_id, ids_item_list = ids_list))
            session.commit()
            
    def __str__(self):
        return '%s: %s, %s' % (self.id_user, self.id_item, self.count)

class Order(Base):
    __tablename__ = 'order'
    
    id = Column(Integer, primary_key = True, nullable = False)
    id_user = Column(Integer, ForeignKey('user.id'), nullable = False)
    ids_item_list = Column(ARRAY(Integer), nullable=True)
    date = Column(String, default = datetime.now().strftime("%d.%m.%Y --> %H:%M"))
    string_id_user = cast(id_user, String)
    link_to_list_items = column_property(f'http://{MAIN_URL}/order/' + string_id_user)
    
    user = relationship(User, backref = 'order')
    
    def __str__(self):
        return '%s: %s, %s, %s, %s' % (
            self.id,
            self.id_user,
            self.date,
            self.string_id_user,
            self.link_to_list_items
        )
    
    def check_id_user(user_id: int) -> bool:
        with session:
            if session.query(Order).filter(Order.id_user == user_id).count() >= True:
                return True
        
    def paid(user_id: int) -> float:
        total = 0
        paid_total = Bascket.join_bascket_item(user_id).filter(and_(Bascket.id_user == user_id, Bascket.paid_status == True)).all()
        for bascket, item in paid_total:
            amount_by_quantity = item.price * bascket.count
            total += amount_by_quantity
        return "{:.2f}".format(round(total, 2))
        
    
    def payment_orders(user_id: int) -> dict:
        with session:
            inner_join_query = session.query(Bascket, Item, Order).join(Bascket, Item.id == Bascket.id_item)
            order_data = dict()
            order = session.query(Order).filter(Order.id_user == user_id)
            for order_pararms in order:
                order_list = list()
                order_id = order_pararms.id
                bascket_ids = order_pararms.ids_item_list
                for bascket_id in bascket_ids:
                    paid_item = inner_join_query.filter(Bascket.id == bascket_id).all()
                    for bascket, item, order in paid_item:
                        items_params = {
                            'bascket_id': bascket.id,
                            'item_id': item.id,
                            'name': item.name,
                            'index': item.index,
                            'price': item.price,
                            'count': bascket.count
                        }
                    order_list.append(items_params)
                order_data.update({order_id: order_list})
            return order_data
