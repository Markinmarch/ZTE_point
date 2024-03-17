from flask import render_template
from settings import dp


@dp.route('/')
def home():
    return render_template('home_page.html')