from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image, image_attachment

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
    name = Column(String(length = 40), default = None, nullable = False)
    phone = Column(String, default = None, nullable = False)
    email = Column(String, default = None, nullable = False, unique = True)
    password = Column(String, default = None, nullable = False)
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
       
    def insert_user(
        user_name: str,
        user_phone: str,
        user_email: str,
        user_password: str,
        user_role: str
    ) -> None:
        session.add(
            User(
                name = user_name,
                phone = user_phone,
                email = user_email,
                password = generate_password_hash(user_password),
                role = user_role
        ))
        session.commit()
        session.close()
        
    def get_user(
        user_id: int
    ):  
        return session.query(User).filter_by(id = user_id).first()
        
  
    def check_email(
        user_email: str
    ) -> bool:
        # так как наши адреса почты уникальные (unique = True) и не может быть больше одного в БД,
        # мы можем по количеству == 1, определить, что запись имеется.
        check_email = session.query(User).filter_by(email = user_email).count()
        if check_email == True:
            return True

    def check_user(
        user_email: str,
        user_password: str
    ):
        get_user_by_email = session.query(User).filter_by(email = user_email)
        user = get_user_by_email.first()
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
    image = image_attachment('ItemImage')

    def __str__(self):
        return '%s: %s, %s, %s' % (self.id, self.name, self.price, self.index)
    
    def get_items():
        return session.query(Item).all()

class ItemImage(Base, Image):
    '''
    ?
    '''
    __tablename__ = 'item_image'
    
    item_id = Column(Integer, ForeignKey('item.id'), primary_key = True)
    
    item = relationship(Item, backref = 'item_image')
    
    # def add_image(self):
    #     self.open_file()

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