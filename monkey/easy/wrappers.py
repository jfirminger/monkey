import dill as pickle

class EasyModel(object):
            def __init__(self, model_name, path="./.models/"):
                directory = path+model_name
                self.model = pickle.load(open(directory+"/"+model_name+".pkl", 'rb'))
                self.func = pickle.load(open(directory+"/"+model_name+"-wrapper.pkl", 'rb'))
            def predict(self, X):
                result = self.func(X, self.model)
                return result

class MonkeyModel(object):
        def __init__(self, model_name, config, path="./models/"):
            """
            example config = {
                "model_name" : "demo",
                "model_objects" : { 
                    "names" : ["model1", "model2"]
                },
                
                "artifacts" : {
                    "names" : ["word2index", "index2word"]
                }
            }

            """
            directory = path+config["model_name"]
          
            self.models = self._get_dependencies(config=config, 
                                                dependency_type="model_objects", 
                                                directory=directory)

            self.artifacts = self._get_dependencies(config=config, 
                                                dependency_type="artifacts", 
                                                directory=directory)

            self.func = pickle.load(open(directory+"/"+model_name+"-wrapper.pkl", 'rb'))
                
        def _get_dependencies(self, config, dependency_type, directory):
            dependencies = {}
            for d in config[dependency_type]["names"]:
                dependencies[d] = pickle.load(open(directory+"/"+d+".pkl", 'rb'))
            
            return dependencies

        def predict(self, X):
            return self.func(X, self.models, self.artifacts)
