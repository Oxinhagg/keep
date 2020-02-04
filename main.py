from app import app
from main_blueprint.blueprint import main_blueprint
from main_api.view import main_api

app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(main_api, url_prefix='/#home')

if __name__ == '__main__':
    app.run()
