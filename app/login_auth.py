from flask import request, render_template, redirect
from flask_login import login_user, current_user

from .app_settings import dp, login_manager
from DB.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

@dp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_data = request.json
        email = login_data['email'],
        password = login_data['password']
        try:
            if User.check_email(email) == True:
                validate_user = User.check_user(
                    email,
                    password            
                )
                if validate_user == True:
                    login_user(validate_user)
                    return redirect('/')
        except TypeError:
            return 'false'
    return render_template('login.html')
