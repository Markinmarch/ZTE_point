from flask import request, render_template
from flask_login import login_required

from app.app_settings import dp, login_manager
from DB.models import Item, User, session


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    items = Item.get_items()
    return render_template('items.html', data = items)

@dp.route('/items', methods = ['POST'])
def search_items():
    pass