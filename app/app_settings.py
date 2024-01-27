from flask import Flask


# общие настройки Фласка
engine = Flask(__name__, template_folder = '../templates', static_folder = '../static')
