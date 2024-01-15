import logging
import os
from dotenv import load_dotenv


def logger():
    if 'ZTE_point.log' not in os.listdir('.'):
        with open('ZTE_point.log', mode = 'x', encoding = 'utf-8') as log_file:
            log_file.close()
    else:
        callable(logging.basicConfig(
            filename = f'ZTE_point.log',
            filemode = 'w',
            format = '%(asctime)s %(levelname)s %(message)s',
            level = logging.INFO
        ))

def main():
    from DB import session
    session
