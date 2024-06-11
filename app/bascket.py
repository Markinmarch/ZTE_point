from flask import request, render_template, redirect
from flask_login import login_required, current_user

from app.app_settings import dp
from DB.models import Item, Bascket


@dp.route('/bascket')
@login_required
def bascket():
    user_bascket = Bascket.not_paid_item_list(user_id = current_user.get_id())
    ready_to_paid_item_list = []
    for item_in_bascket in user_bascket:
        data = Item.established_items_list(id = item_in_bascket['item_id'])
        data_list = ready_to_paid_item_list.append(data)   
    return render_template('bascket.html', data = data_list)