from flask import request, render_template
from flask_login import login_required, current_user

from app.app_settings import dp
from DB.models import Item, Order


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    items = Item.get_items()
    if request.method == 'POST':
        item_id = request.form['id']
        item_count = request.form['count']
        Order.add_items(
            id_user_arg = current_user.get_id(),
            id_item_arg = item_id,
            count_arg = item_count
        )
    return render_template('items.html', items_data = items)

@dp.route('/items/search', methods = ['GET', 'POST'])
def search_item():
    if request.method == 'POST':
        item_id = request.form['id']
        item_count = request.form['count']
        Order.add_items(
            id_user_arg = current_user.get_id(),
            id_item_arg = item_id,
            count_arg = item_count
        )
    keywords = request.args.get('keywords')
    keywords_list = [keyword.lower() for keyword in keywords.split()]
    set_keywords = set(keywords_list)
    search_item = Item.search_items(keywords = set_keywords)
    return render_template('items.html', search_items_data = search_item)