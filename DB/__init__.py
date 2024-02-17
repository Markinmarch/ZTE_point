from .models import create_database
from config import postgres_user, postgres_database, postgres_host, postgres_password, postgres_port


database = create_database(
    user = postgres_user,
    password = postgres_password,
    host = postgres_host,
    port = postgres_port,
    database = postgres_database
)
