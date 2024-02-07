from flask import request, render_template, Response, app

from .app_settings import dp
from DB.db_main import insert_user
from . import home_page


@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['userName']
        phone = request.form['userPhone']
        email = request.form['userEmail']
        password = request.form['userPassword']
        insert_user(
            user_name = name,
            user_phone = phone,
            user_email = email,
            user_password = password
        )
        return dp.add_url_rule('/', 'home_page', home_page.home())
    else:
        return render_template('registration.html')