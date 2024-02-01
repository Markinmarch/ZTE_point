from flask import request, render_template
from .app_settings import dp


@dp.route('/items', methods = ['GET', 'POST'])
def items():
    pass