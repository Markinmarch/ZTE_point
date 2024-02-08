from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

from DB.db_models import User, Item, Order, create_table
from . import (
    postgres_user,
    postgres_password,
    postgres_host,
    postgres_port,
    postgres_database
)


DSN = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (postgres_user, postgres_password, postgres_host, postgres_port, postgres_database )
engine = create_engine(DSN)
tables = create_table(engine)

Session = sessionmaker(engine)
session = Session()

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
            password = generate_password_hash(user_password)
    ))
    session.commit()
    session.close()

def check_user(
    user_email: int,
    user_password: str
) -> bool:
    return session.query(User).filter(User.email == user_email), check_password_hash(hash, user_password)
            

# def delete_user():
#     pass

# def inser_item():
#     pass

# def select_item():
#     pass

# def add_order():
#     pass

