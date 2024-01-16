import logging
import os
from dotenv import load_dotenv


def logger():
    if 'ZTE_point.log' not in os.listdir('.'):
        with open('ZTE_point.log', mode = 'x', encoding = 'utf-8') as log_file:
            log_file.close()
    else:
        pass

    logging.basicConfig(
        format = '%(asctime)s %(name)s %(levelname)s %(message)s',
        level = logging.INFO,
        handlers = [
            logging.FileHandler('ZTE_point.log'),
            logging.StreamHandler()
        ]
    )

def main():
    from DB import session, create_database
    create_database
    session
