from flask import Flask
from flask_login import LoginManager

from config import SECRET_WORD


# общие настройки Фласка
dp = Flask(__name__, template_folder = '../templates', static_folder = '../static')
login_manager = LoginManager(dp)
login_manager.init_app(dp)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'
dp.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
dp.config.update(
    TESTTING = True,
    SECRET_KEY = SECRET_WORD,
)
