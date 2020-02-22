import pytest

from app import create_app

# flask_app = connexion.FlaskApp(__name__)
# flask_app.add_api('swagger.yml')


@pytest.fixture(scope='module')
def client():
    app = create_app()
    with app.test_client() as c:
        yield c