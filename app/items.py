from flask import request, render_template
from flask_login import login_required, current_user

from app.app_settings import dp
from DB.models import Item, Bascket


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    items = Item.get_items()
    if request.method == 'POST':
        item_id = request.form['id']
        item_count = request.form['count']
        Bascket.add_items(
            user_id = current_user.get_id(),
            item_id = item_id,
            item_count = item_count
        )
        
    return render_template('items.html', items_data = items)

@dp.route('/items/search', methods = ['GET', 'POST'])
def search_item():
    if request.method == 'POST':
        item_id = request.form['id']
        item_count = request.form['count']
        Bascket.add_items(
            user_id = current_user.get_id(),
            item_id = item_id,
            item_count = item_count
        )
    keywords = request.args.get('keywords')
    keywords_list = [keyword.lower() for keyword in keywords.split()]
    set_keywords = set(keywords_list)
    search_item = Item.search_items(keywords = set_keywords)
    return render_template('items.html', search_items_data = search_item, reset_search = True)