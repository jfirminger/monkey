from datetime import datetime
import getpass
import json
from os.path import join, exists
from os import listdir


class MonkeyLog():
    def __init__(self, directory, log_type=None):
        timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        self.file_name = "monkey.json"

        if exists(directory) and self.file_name in listdir(directory):
            self.json_out = json.load(open(join(directory, self.file_name)))
        else:
            self.json_out = {
                "type" : log_type,
                "location" : directory,
                "user" : getpass.getuser(),
                "timestamp" : timestamp,
                "content" : {
                    "models" : [],
                    "models_type" : [],
                    "artifacts" : [],
                    "wrapper" : ""
                }
            }
    
    def add_model(self, model_file, model_type):
        self.json_out["content"]["models"].append(model_file)
        self.json_out["content"]["models_type"].append(model_type)
    
    def add_artifact(self, artifact_file):
        self.json_out["content"]["artifacts"].append(artifact_file)

    def add_wrapper(self, wrapper_file):
        self.json_out["content"]["wrapper"] = wrapper_file

    def get_models(self):
        return self.json_out["content"]["models"], self.json_out["content"]["models_type"]

    def get_artifacts(self):
        return self.json_out["content"]["artifacts"]

    
    def get_wrapper(self):
        return self.json_out["content"]["wrapper"]

    def save_log(self):
        with open(join(self.json_out["location"], self.file_name), "w") as f:
            print(self.json_out)
            json.dump(self.json_out, f)