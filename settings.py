from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin

from config import SECRET_WORD


# общие настройки Фласка
dp = Flask(__name__, template_folder = '../templates', static_folder = '../static')
login_manager = LoginManager()
login_manager.init_app(dp)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'
dp.config.update(
    TESTTING = True,
    SECRET_KEY = SECRET_WORD,
    FLASK_ADMIN_SWATCH = 'cerulean',
    SEND_FILE_MAX_AGE_DEFAULT = 0
)
admin = Admin(dp, name = 'parts_shop')
# admin.init_app(dp)