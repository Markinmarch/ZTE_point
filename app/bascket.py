from flask import request, render_template, redirect
from flask_login import login_required, current_user

from app.app_settings import dp
from DB.models import Bascket


@dp.route('/bascket', methods = ['POST', 'GET'])
@login_required
def bascket():
    if request.method == 'POST':
        item_id = request.form['id']
        Bascket.delete_item(
            user_id = current_user.get_id(),
            item_id = item_id
        )
    user_bascket = Bascket.not_paid_item_list(user_id = current_user.get_id())
    if user_bascket == []:
        bascket_status = False
    else:
        bascket_status = True
    return render_template('bascket.html', data = user_bascket, bascket_status = bascket_status)

# @dp.route('/bascket/payment', methods = ['POST', 'GET'])
# @login_required
# def payment():
#     user_bascket = Bascket.not_paid_item_list(user_id = current_user.get_id())
#     return render_template('bascket.html', data = user_bascket)