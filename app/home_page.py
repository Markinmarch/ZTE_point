from flask import render_template
from flask_login import current_user

from app.app_settings import dp
from DB.models import Order


def check_status() -> list[dict[str, str]] | None:
    if current_user.is_authenticated:
        nav_data = [{
            'status': '<a class = "login" type = "button" href = "/logout">Выйти</a><a id = "nav_href_bascket" class = "bascket" type = "button" href = "/bascket"><img src="https://t700.ru/icon/cart.png" width="44" height="44,5""></a>'
        }]
        if Order.check_id_user(current_user.get_id()) == True:
            nav_data.append({
                'orders': f'<a id = "nav_href_order" class = "bascket" type = "button" href = "/orders/{current_user.get_id()}"><img src="https://www.seekpng.com/png/full/542-5420406_the-shipped-icon-is-a-plain-black-and.png" width="52" height="33" vspace="5"></a>'
                })
        if current_user.is_admin() == True:
            nav_data = [{
                'status': '<a class = "login" type = "button" href = "/logout">Выйти</a><a class = "login" type = "button" href = "/admin">Админка</a>'
            }]
            return nav_data
        return nav_data

@dp.route('/')
def home():
    if check_status() is None:
        nav_data = [{
            'status': '<a class = "login" type = "button" href = "/login">Войти</a>'
        }]
    else: 
        nav_data = check_status()
    return render_template('home_page.html', nav_data = nav_data)