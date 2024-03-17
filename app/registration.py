from flask import request, render_template, redirect

from .app_settings import dp
from DB.models import User


@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_datas = request.json
        email = user_datas['email']
        name = user_datas['name']
        phone = user_datas['phone']
        password = user_datas['password']
        if User.check_email(email) == True:
            return 'false'
        else:
            User.insert_user(
                user_name = name,
                user_phone = phone,
                user_email = email,
                user_password = password
            )
    return render_template('registration.html')
