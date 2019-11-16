import pytest
from monkey.application import PredictionServer
import sys, os
from os.path import dirname, join


@pytest.fixture
def test_prediction_server_model_0():
    model_name = "TestModel"
    sys.path.insert(1, join(dirname(__file__), "model_test_0"))
    app = PredictionServer(model_name, {})._create_application()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['DEBUG'] = False
    app = app.test_client()

    return app
