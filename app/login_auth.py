from flask import request, render_template, redirect
from flask_login import login_user

from .app_settings import dp, login_manager
from DB.models import User


@dp.route('/login', methods = ['GET', 'POST'])
@login_manager.user_loader
def login():
    if request.method == 'POST':
        join_user = User.check_user(
            user_email = request.form['userEmail'],
            user_password = request.form['userPassword']            
        )
        if join_user != False:
            login_user(join_user)
            return redirect('/')
        return 'false'
    return render_template('login.html')