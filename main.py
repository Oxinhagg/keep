from app import app
from app import db
from test_blueprint.blueprint import test_blueprint


import view


app.register_blueprint(test_blueprint, url_prefix='/test_blueprint')


if __name__ == '__main__':
    app.run()
