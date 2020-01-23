from app import app
from flask import render_template

from models import Keep


@app.route('/')
def index():
    keeps = Keep.query.all()
    return render_template('index.html', keeps=keeps)


@app.route('/<slug>')
def keep_detail(slug):
    keep = Keep.query.filter(Keep.slug == slug).first()
    return render_template('keep_detail.html', keep=keep)
