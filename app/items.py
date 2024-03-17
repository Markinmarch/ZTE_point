from flask import request, render_template
from flask_login import login_required

from .app_settings import dp


@dp.route('/items', methods = ['GET', 'POST'])
@login_required
def items():
    return 'qwerty'