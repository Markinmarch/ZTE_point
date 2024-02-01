import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from .db_config import DataBase


load_dotenv(dotenv_path = '.env')

postgres_password = os.getenv('POSTGRES_PASSWORD', '')
postgres_user = 'postgres'
postgres_host = 'localhost'
postgres_port = '5432'
postgres_database = 'main_db'

database = DataBase(
    user = postgres_user,
    password = postgres_password,
    host = postgres_host,
    port = postgres_port,
    database = postgres_database
)

create_database = database.create_database()
engine = database.sql_engine()
create_tables = database.add_tables()

Session = sessionmaker(bind = engine)
session = Session()