from flask import request, render_template
from flask_login import login_required

from .app_settings import dp
from .app_settings import dp, login_manager
from DB.models import User, session


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    return render_template('shop.html')