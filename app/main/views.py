from flask import render_template
from . import main
from flask_login import current_user
from ..models import User


@main.route('/')
def index():
    usuarios = []
    if current_user.is_authenticated:
        usuarios = User.query.order_by(User.username).all()
    return render_template('index.html', usuarios=usuarios)