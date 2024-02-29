from flask import request, render_template, redirect, jsonify, after_this_request, stream_template_string
import json

from .app_settings import dp
from DB.models import User


@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        name = request.form['userName']
        phone = request.form['userPhone']
        email = request.form['userEmail']
        password = request.form['userPassword']
        if User.check_email(email) == True:
            return redirect(f'/registration?status=email_is_busy')
        else:
            User.insert_user(
                user_name = name,
                user_phone = phone,
                user_email = email,
                user_password = password
            )
            return redirect('/?status=ok')
