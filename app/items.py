from flask import request, render_template
from .app_settings import engine


@engine.route('/items', methods = ['GET', 'POST'])
def items():
    pass