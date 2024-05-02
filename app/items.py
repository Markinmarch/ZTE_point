from flask import request, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import BadRequestKeyError

from app.app_settings import dp
from DB.models import Item


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    items = Item.get_items()
    if request.method == 'POST':
        try:
            words = request.form['itemSearch']
            if words == '':
                return redirect('/items')
            words_list = [word.lower() for word in words.split()]
            keywords = set(words_list)
            search_items = Item.search_items(keywords = keywords)
            return render_template('items.html', items_data = items, search_items_data = search_items)
        except BadRequestKeyError:
            return render_template('items.html', items_data = items)
    return render_template('items.html', items_data = items)