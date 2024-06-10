from flask import request, render_template, redirect
from flask_login import login_required, current_user

from app.app_settings import dp
from DB.models import Item, Bascket


@dp.route('/bascket')
@login_required
def bascket():
    user_bascket = Bascket.not_paid_item_list(user_id = current_user.get_id())
    return render_template('bascket.html', data = user_bascket)