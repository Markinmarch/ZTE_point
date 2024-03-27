from flask import render_template
from flask_login import current_user

from .app_settings import dp
from DB.models import User


@dp.route('/')
def home():
    if current_user.is_authenticated:
        data = [{
            'context': '<a class = "login" type = "button" href = "/logout">Выйти</a><a class = "bascket" type = "button" href = "/bascket"><img src="https://t700.ru/icon/cart.png" width="42" height="42"></a>'
        }]
    else:
        data = [{
            'context': '<a class = "login" type = "button" href = "/login">Войти</a>'
        }]
    return render_template('home_page.html', data = data)