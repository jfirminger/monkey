import pytest
from monkey.service.application import PredictionServer
from monkey.easy.decorators import easy_wrap, monkey_wrap
from monkey.easy.wrappers import EasyModel, MonkeyModel
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

@pytest.fixture
def test_easy_wrap_local():
    return easy_wrap
    
@pytest.fixture
def test_easy_model_class():
    return EasyModel

@pytest.fixture
def test_monkey_wrap_local():
    return monkey_wrap

@pytest.fixture
def test_monkey_model_class():
    return MonkeyModel