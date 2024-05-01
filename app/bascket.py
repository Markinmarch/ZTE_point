from flask import request, render_template, redirect
from flask_login import login_required

from app.app_settings import dp
from DB.models import Item


@dp.route('/bascket')
@login_required
def bascket():
    return render_template('bascket.html')