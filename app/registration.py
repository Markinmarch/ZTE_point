from flask import request, render_template

from .app_settings import dp
from DB.db_main import insert_user


@dp.route('/registration', methods = ['POST', 'GET'])
def registration():
    insert_user(
        user_name = request.form['userName'],
        user_phone = request.form['userPhone'],
        user_email = request.form['userEmail'],
        user_password = request.form['userPassword']
    )
    return render_template('registration.html')