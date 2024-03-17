from flask import request, render_template, redirect
from flask_login import login_user, current_user

from .app_settings import dp, login_manager
from DB.models import User


@dp.route('/login', methods = ['GET', 'POST'])
@login_manager.user_loader
def login():
    if request.method == 'POST':
        user_email = request.form['userEmail'],
        user_password = request.form['userPassword'] 
        validate_user = User.check_user(
            user_email,
            user_password            
        )
        print(validate_user)
        if bool(validate_user) == True:
            login_user(validate_user)
            return redirect('/')
        return 'false'
    return render_template('login.html')