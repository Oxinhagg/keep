from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


import config
from .keep.models import db
from .keep.views import main_api, ma


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Configuration)

    CORS(app)

    db.init_app(app)

    app.register_blueprint(main_api, url_prefix='/keep')

    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    ma.init_app(app)

    return app
