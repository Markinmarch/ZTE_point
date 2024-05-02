from flask import request, render_template, redirect
from flask_login import login_required

from app.app_settings import dp
from DB.models import Item


@dp.route('/items')
@login_required
def items():
    items = Item.get_items()
    return render_template('items.html', items_data = items)

@dp.route('/items', methods = ['POST'])
@login_required
def search_item():
    items = Item.get_items()
    words = request.form['itemSearch']
    if words == '':
        return redirect('/items')
    words_list = [word.lower() for word in words.split()]
    keywords = set(words_list)
    search_items = Item.search_items(keywords = keywords)
    return render_template('items.html', items_data = items, search_items_data = search_items)
    
# @dp.route('/items', method = ['POST'])
# @login_required
# def add_items_id_bascket():
#     add_item = request.form['itemBuy']
#     print(add_item)