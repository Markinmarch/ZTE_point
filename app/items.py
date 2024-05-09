from flask import request, render_template, redirect
from flask_login import login_required, current_user
from werkzeug.exceptions import BadRequestKeyError

from app.app_settings import dp
from DB.models import Item, Order


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    items = Item.get_items()
    if request.method == 'POST':
        try:
            words = request.form['itemSearchInput']
            if words == '':
                return redirect('/items')
            words_list = [word.lower() for word in words.split()]
            keywords = set(words_list)
            search_items = Item.search_items(keywords = keywords)
            return render_template('items.html', items_data = items, search_items_data = search_items)
        except BadRequestKeyError or KeyError:
            item_id = request.form['itemId']
            item_count = request.form['itemCount']
            Order.add_items(
                id_user_arg = current_user.get_id(),
                id_item_arg = item_id,
                count_arg = item_count
            )
            # return render_template('items.html', items_data = items, search_items_data = search_items)
    return render_template('items.html', items_data = items)


# @dp.route('/items', methods = ['GET', 'POST'])
# @login_required
# def items():
#     items = Item.get_items()
#     if request.method == 'POST':
#         # try:
#         #     words = request.form['itemSearchInput']
#         #     print(words)
#         #     if words == '':
#         #         return redirect('/items')
#         #     words_list = [word.lower() for word in words.split()]
#         #     keywords = set(words_list)
#         #     search_items = Item.search_items(keywords = keywords)
#         #     return render_template('items.html', items_data = items, search_items_data = search_items)
#         # except KeyError:
#             item_id = request.form['id']
#             item_count = request.form['count']
#             print(item_count)
#             print(item_id)
#             Order.add_items(
#                 id_user_arg = current_user.get_id(),
#                 id_item_arg = item_id,
#                 count_arg = item_count
#             )
#             return render_template('items.html', items_data = items)
#     return render_template('items.html', items_data = items)