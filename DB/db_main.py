from . import session
from .db_models import User, Item, Order


def insert_user(
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
            password = user_password
    ))
    session.commit()
    session.close()

def select_user(user_id: int) -> str:
    return session.query(User).filter(User.id == user_id)
            

def delete_user():
    pass

def inser_item():
    pass

def select_item():
    pass

def add_order():
    pass

