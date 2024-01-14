import logging
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv(dotenv_path = '.env')

postgres_password = os.getenv('POSTGRES_PASSWORD', '')
postgres_user = 'postgres'
postgres_host = 'localhost'
postgres_port = '5432'
postgres_database = 'main_db'

now_time = datetime.now().strftime('%m/%d/%y_%H:%M:%S')

logger = logging.basicConfig(
    filename = f'ZTE_point_{now_time}.log',
    filemode = 'w',
    format = '%(asctime)s %(levelname)s %(message)s',
    level = logging.INFO
)