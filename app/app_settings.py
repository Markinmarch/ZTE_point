from flask import Flask
from flask_login import LoginManager, login_user, logout_user, login_required


# общие настройки Фласка
dp = Flask(__name__, template_folder = '../templates', static_folder = '../static')
login_manager = LoginManager(dp)
login_manager.init_app(dp)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'
