from . import db_models
from . import db_config

import os
from dotenv import load_dotenv
from DB.config import create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv(dotenv_path = '.env')

postgres_password = os.getenv('POSTGRES_PASSWORD', '')
postgres_user = 'postgres'
postgres_host = 'localhost'
postgres_port = '5432'
postgres_database = 'main_db'


DSN = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (postgres_user, postgres_password, postgres_host, postgres_port, postgres_database )
engine = create_engine(DSN)

Session = sessionmaker(engine)
session = Session()

database = create_database(
    user = postgres_user,
    password = postgres_password,
    host = postgres_host,
    port = postgres_port,
    database = postgres_database
)
