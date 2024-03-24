from flask import request, render_template, redirect

from .app_settings import dp
from DB.models import User


@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_data = request.json
        email = user_data['email']
        name = user_data['name']
        phone = user_data['phone']
        password = user_data['password']
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
