from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from test_blueprint.blueprint import test_blueprint

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

app.register_blueprint(test_blueprint, url_prefix='/test_blueprint')