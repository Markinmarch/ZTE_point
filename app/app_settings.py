from flask import Flask
from flask_login import UserMixin, LoginManager


# общие настройки Фласка
dp = Flask(__name__, template_folder = '../templates', static_folder = '../static')
login_manager = LoginManager(app=dp)