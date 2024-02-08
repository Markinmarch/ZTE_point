from flask import request, render_template, redirect
from .app_settings import dp

from DB.db_main import check_user


@dp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        x = check_user(
            user_email = request.form['userEmail'],
            user_password = request.form['userPassword']            
        )
        print(x)
        return redirect('/')
    else:
        return render_template('login.html')