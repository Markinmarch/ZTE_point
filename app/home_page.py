from flask import render_template
from flask_login import current_user

from app.app_settings import dp
from DB.models import Order

''''''
@dp.route('/')
def home():
    print(f'++++++++++++++++++++++++++++++++++++++++={current_user.get_id()}')
    if current_user.is_authenticated:
        data = [{
            'status': '<a class = "login" type = "button" href = "/logout">Выйти</a><a class = "bascket" type = "button" href = "/bascket"><img src="https://t700.ru/icon/cart.png" width="42" height="42"></a>'
        }]
        if current_user.is_admin() == True:
            data = [{
                'status': '<a class = "login" type = "button" href = "/logout">Выйти</a><a class = "bascket" type = "button" href = "/bascket"><img src="https://t700.ru/icon/cart.png" width="42" height="42"></a><a class = "login" type = "button" href = "/admin">Админка</a>'
            }]
            if Order.check_id_user(current_user.get_id()) == True:
                data.append({
                    'orders': '<a class = "bascket" type = "button" href = "/bascket"><img src="https://t700.ru/icon/cart.png" width="42" height="42"></a>'
                })
    else:
        data = [{
            'status': '<a class = "login" type = "button" href = "/login">Войти</a>'
        }]

    return render_template('home_page.html', data = data)