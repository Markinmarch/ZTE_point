from flask import request, render_template, Response, redirect

from .app_settings import dp
from DB.models import User


@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    if request.method == 'POST':
        name = request.form['userName']
        phone = request.form['userPhone']
        email = request.form['userEmail']
        password = request.form['userPassword']
        if User.check_email(email) == True:
            data = {'status': 'email_is_busy'}
            return render_template('registration.html', data = data)
        else:
            User.insert_user(
                user_name = name,
                user_phone = phone,
                user_email = email,
                user_password = password
            )
            context = {'status': 'OK'}
            return redirect('/')