from . import models

from . models import create_database
from config import (
    POSTGRES_USER,
    POSTGRES_DATABASE,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT)


database = create_database(
    user = POSTGRES_USER,
    password = POSTGRES_PASSWORD,
    host = POSTGRES_HOST,
    port = POSTGRES_PORT,
    database = POSTGRES_DATABASE
)
