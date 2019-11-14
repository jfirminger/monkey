from monkey.application import PredictionServer
import sys, os
import unittest
from os.path import dirname, join
import requests

class TestServerModelTest0(unittest.TestCase):

    def setUp(self):
        self.model_name = "TestModel"

        sys.path.insert(1, join(dirname(__file__), "model_test_0"))
        app = PredictionServer(self.model_name, {})._create_application()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_predict_post(self):
        data = '[1,2,3]'
        response = self.app.post('/predict', data="%s" % data, 
                headers={"Content-Type": "application/json"})
        
        assert response.status_code == 200

        assert response.json == {
            "results" : 6
        }
        
    def test_predict_get(self):
        response = self.app.get('/predict')
        
        assert response.status_code == 200

        assert response.json == "{} model is here".format(self.model_name)
        
if __name__ == '__main__':
    unittest.main()