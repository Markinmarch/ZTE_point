from flask import request, render_template, redirect
from flask_login import login_required, current_user

from sqlalchemy.exc import NoResultFound

from app.app_settings import dp
from DB.models import Bascket


@dp.route('/bascket', methods = ['POST', 'GET'])
@login_required
def bascket():
    if request.method == 'POST':
        item_id = request.form['id']
        item_count = request.form['count']
        Bascket.update_before_payment(
            user_id = current_user.get_id(),
            item_id = item_id,
            item_count = item_count
        )
    user_bascket = Bascket.not_paid_item_list(Bascket, user_id = current_user.get_id())
    if user_bascket == []:
        bascket_status = False
    else:
        bascket_status = True
    return render_template('bascket.html', data = user_bascket, bascket_status = bascket_status)

@dp.route('/bascket/delete_item', methods = ['POST', 'GET'])
def delete_item():
    try:
        delete_item_id = request.args.get('delete_item_id')
        Bascket.delete_item(
            user_id = current_user.get_id(),
            item_id = delete_item_id
        )
    except NoResultFound:
        pass
    return redirect('/bascket')


@dp.route('/bascket/payment', methods = ['POST', 'GET'])
def payment():
    if request.method == 'POST':
        user_id = current_user.get_id()
        Bascket.payment(user_id)
        return render_template('bascket.html', bascket_status = False)
    user_bascket = Bascket.not_paid_item_list(Bascket, user_id = current_user.get_id())
    total_price = Bascket.total_price(Bascket, user_id = current_user.get_id())
    return render_template('payment.html', total_price = total_price, data = user_bascket)