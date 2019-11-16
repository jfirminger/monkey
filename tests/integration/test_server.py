def test_predict_post(test_prediction_server_model_0):
    """
    GIVEN a model contract and Flask application
    POST on '/predict'
    THEN check result is valid
    """
    data = '[1,2,3]'
    response = test_prediction_server_model_0.post('/predict', data="%s" % data, 
                headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json == {
            "results" : 6
    }

def test_predict_get(test_prediction_server_model_0):
    """
    GIVEN a model contract and Flask application
    GET on '/predict' 
    THEN check result is valid 
    """
    response = test_prediction_server_model_0.get('/predict')
        
    assert response.status_code == 200
    assert response.json == "{} model is here".format(
        "TestModel")

