from flask import request, render_template, redirect
from .app_settings import dp, login_manager

from DB.models import User, session


@dp.route('/login', methods = ['GET', 'POST'])
@login_manager.user_loader
def login_auth():
    if request.method == 'POST':
        check = User.check_user(
            user_email = request.form['userEmail'],
            user_password = request.form['userPassword']            
        )
        print(session.query(User).filter(User.email == request.form['userEmail']))
        return check
    else:
        return render_template('login.html')