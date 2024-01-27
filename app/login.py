from flask import request, render_template
from .app_settings import engine


@engine.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # username = request.form['username']
        # password = request.form['password']
        return 'Вы вошли в систему'
    else:
        return render_template('login.html')
    # return render_template('base.html')