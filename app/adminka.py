from flask import redirect, render_template

from flask_login import current_user

# from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from app.app_settings import admin #, staff
from DB.models import User, Item, session


admin.add_view(ModelView(User, session))
admin.add_view(ModelView(Item, session))



from flask import render_template
from flask_login import current_user

from app.app_settings import dp




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