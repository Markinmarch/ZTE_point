from flask import request, render_template, redirect, jsonify, after_this_request, stream_template_string
import json

from .app_settings import dp
from DB.models import User


@dp.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # name = request.form['userName']
        # phone = request.form['userPhone']
        # email = request.form['userEmail']
        # password = request.form['userPassword']
        email = request.form["email"]
        print(email)
        if User.check_email(email) == True:
            return jsonify('email_is_busy')
        # else:
        #     User.insert_user(
        #         user_name = name,
        #         user_phone = phone,
        #         user_email = email,
        #         user_password = password
        #     )
        #     return redirect('/')
    return render_template('registration.html')
