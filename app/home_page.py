from flask import render_template
from .app_settings import dp


@dp.route('/')
def home():
    return render_template('home_page.html')