from flask import request, render_template, redirect
from flask_login import login_required, current_user

from sqlalchemy.exc import NoResultFound

from app.app_settings import dp
from DB.models import Bascket


@dp.route('/bascket', methods = ['POST', 'GET'])
@login_required
def bascket():
    if request.method == 'POST':
        try:
            item_id = request.form['itemId']
            Bascket.delete_item(
                user_id = current_user.get_id(),
                item_id = item_id
            )
        except NoResultFound:
            pass
    user_bascket = Bascket.not_paid_item_list(Bascket, user_id = current_user.get_id())
    if user_bascket == []:
        bascket_status = False
    else:
        bascket_status = True
    return render_template('bascket.html', data = user_bascket, bascket_status = bascket_status)

@dp.route('/bascket/payment', methods = ['POST', 'GET'])
@login_required
def payment():
    if request.method == 'POST':
        item_id = request.form['id']
        item_count = request.form['count']
        print(item_id, item_count)
    user_bascket = Bascket.not_paid_item_list(Bascket, user_id = current_user.get_id())
    if user_bascket == []:
        bascket_status = False
    else:
        bascket_status = True
    tatal_price = Bascket.tatal_price(Bascket, user_id = current_user.get_id())
    return render_template('bascket.html', total_price = tatal_price, data = user_bascket, bascket_status = bascket_status)