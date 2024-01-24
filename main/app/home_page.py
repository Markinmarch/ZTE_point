from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main/templates/base.html')