from flask import Blueprint
from flask import render_template

test_blueprint = Blueprint('test_blueprint', __name__, template_folder='templates')

@test_blueprint.route('/')
def index():
    return render_template('test_blueprint/index.html')