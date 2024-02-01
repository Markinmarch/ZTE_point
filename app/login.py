from flask import request, render_template
from .app_settings import dp


@dp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password in 'aswdwdawdawdawdawdawd':
            return render_template('home_page.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')