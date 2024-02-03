# from . import db_models
# from . import db_main
# from . import db_config

import os
from dotenv import load_dotenv
from DB.db_config import create_database


load_dotenv(dotenv_path = '.env')

postgres_password = os.getenv('POSTGRES_PASSWORD', '')
postgres_user = 'postgres'
postgres_host = 'localhost'
postgres_port = '5432'
postgres_database = 'main_db'

# database = create_database(
#     user = postgres_user,
#     password = postgres_password,
#     host = postgres_host,
#     port = postgres_port,
#     database = postgres_database
# )
