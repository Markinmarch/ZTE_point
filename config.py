import os
import binascii
from dotenv import load_dotenv

load_dotenv(dotenv_path = '.env')

SECRET_WORD = os.getenv('SECRET_WORD', '').encode("utf-8").hex()
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_USER = 'postgres'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_DATABASE = 'main_db'
