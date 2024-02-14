from flask import request, render_template, redirect
from .app_settings import dp

from DB.db_main import check_user


@dp.route('/login', methods = ['GET', 'POST'])
def login_auth():
    if request.method == 'POST':
        x = check_user(
            user_email = request.form['userEmail'],
            user_password = request.form['userPassword']            
        )
        return x
    else:
        return render_template('login.html')