from flask import Flask, request, jsonify
import importlib
import os
from monkey.wsgi import WSGIServer

class Server(object):

    def __init__(self, model_name, options):
        self.model = self._init_model(model_name)()
        self.options = options
        self.application = self._create_application()
        
    def _init_model(self, model_name):
        try:
            interface_file = importlib.import_module(model_name)
            model_class = getattr(interface_file, model_name)
        except Exception as e:
            print(e)
            print("Could not import model {}".format(model_name))
        return model_class

    def _create_application(self):
        application = Flask(__name__)


        @application.route("/predict", methods=["GET","POST"])
        def predict():
            if request.method == "POST":
                json_req = request.json
                results = self.model.predict(json_req)
                return jsonify(results)
            else:
                return "loan model is here."

        return application
        
    def run(self):
        WSGIServer(self.application, self.options).run()