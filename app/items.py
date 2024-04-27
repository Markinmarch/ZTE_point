from flask import request, render_template
from flask_login import login_required

from app.app_settings import dp
from DB.models import Item


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    items = Item.get_items()
    return render_template('items.html', data = items)

@dp.route('/items', methods = ['GET','POST'])
def search_items():
    words = request.form['itemSearch']
    words_list = [word.lower() for word in words.split()]
    keywords = set(words_list)
    items = Item.search_items(keyword = keywords)
    print(items)
    return render_template('items.html', data = items)
