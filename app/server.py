from flask import Flask, request, jsonify
import importlib
import os
from wsgi import WSGIServer

def init_model(model_name):
    try:
        interface_file = importlib.import_module(model_name)
        model_class = getattr(interface_file, model_name)
    except Exception as e:
        print(e)
        print("Could not import model {}".format(model_name))
    return model_class

def create_application(model):
    application = Flask(__name__)


    @application.route("/predict", methods=["GET","POST"])
    def predict():
        if request.method == "POST":
            json_req = request.json
            results = model.predict(json_req)
            return jsonify(results)
        else:
            return "loan model is here."

    return application

if __name__ == "__main__":
    model = init_model(os.getenv("MODEL_NAME"))()

    application = create_application(model)

    options = {
        'bind': '{0}:{1}'.format('0.0.0.0', os.getenv("PORT")),
        'workers': os.getenv("NUM_WORKERS"),
    }

    WSGIServer(application, options).run()