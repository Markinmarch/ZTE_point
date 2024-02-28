from flask import request, render_template, redirect, jsonify, after_this_request
import json

from .app_settings import dp
from DB.models import User


@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html', context = None)
    elif request.method == 'POST':
        name = request.form['userName']
        phone = request.form['userPhone']
        email = request.form['userEmail']
        password = request.form['userPassword']
        if User.check_email(email) == True:
            data = {'status': 'email_is_busy'}
            return render_template('registration.html', context = data)
        else:
            User.insert_user(
                user_name = name,
                user_phone = phone,
                user_email = email,
                user_password = password
            )
            data = {'status': 'OK'}
            return redirect('/')
        
# @dp.route('/registraton/email_is_busy')
# def email_is_busy():
#     return render_template('registration.html', context = {'account_status': 'email_is_busy'})
