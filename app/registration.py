from flask import request, render_template

from .app_settings import dp
from DB.db_main import insert_user


@dp.route('/registration', methods = ['POST', 'GET'])
def registration():
    if request.method == 'POST':
        if request.form['userPassword'] != request.form['repeatPassword']:
            return render_template('registration.html')
        insert_user(
            user_name = request.form['userName'],
            user_phone = request.form['userPhone'],
            user_email = request.form['userEmail'],
            user_password = request.form['userPassword'],
        )
        return render_template('home_page.html')
    else:
        return render_template('registration.html')
