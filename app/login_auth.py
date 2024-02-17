from flask import request, render_template, redirect
from .app_settings import dp

from DB.models import User


@dp.route('/login', methods = ['GET', 'POST'])
def login_auth():
    if request.method == 'POST':
        check = User.check_user(
            user_email = request.form['userEmail'],
            user_password = request.form['userPassword']            
        )
        return check
    else:
        return render_template('login.html')