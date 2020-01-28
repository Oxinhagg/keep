from app import app
from test_blueprint.blueprint import test_blueprint
from main_blueprint.blueprint import main_blueprint


app.register_blueprint(test_blueprint, url_prefix='/test_blueprint')
app.register_blueprint(main_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run()
