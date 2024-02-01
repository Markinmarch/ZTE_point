from flask import Flask


# общие настройки Фласка
dp = Flask(__name__, template_folder = '../templates', static_folder = '../static')
