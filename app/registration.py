from flask import request, render_template
from flask_login import login_user

from app.app_settings import dp, login_manager
from DB.models import User
from config import ADMIN_KEY


@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_data = request.json
        email = user_data['email']
        name = user_data['name']
        phone = user_data['phone']
        password = user_data['password']
        if len(password) < 6:
            return 'few characters'
        if User.check_email(email) == True:
            return 'false'
        if email == ADMIN_KEY:
            User.insert_user(
                user_name = name,
                user_phone = phone,
                user_email = email,
                user_password = password,
                user_role = 'admin'
            )
        else:
            User.insert_user(
                user_name = name,
                user_phone = phone,
                user_email = email,
                user_password = password
            )
        validate_user = User.check_user(
            email,
            password            
        )
        login_user(validate_user)
    return render_template('registration.html')
