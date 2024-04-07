from flask import request, render_template, redirect
from flask_login import logout_user

from app.app_settings import dp, login_manager
from DB.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

@dp.route('/logout')
def logout():
    logout_user()
    return redirect('/')