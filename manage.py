import logging
import os


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
    if __name__ == "__main__":
        from DB.main_db import database, create_table
        from app import app_settings
        database
        create_table
        app_settings.dp.run(debug=True)
logger()
main()