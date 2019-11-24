import dill as pickle
import json
from os import listdir
from os.path import isfile, join


class EasyModel(object):
            def __init__(self, model_name, path="./.models/"):
                directory = path+model_name
                self.model = pickle.load(open(directory+"/"+model_name+".pkl", 'rb'))
                self.func = pickle.load(open(directory+"/"+model_name+"-wrapper.pkl", 'rb'))
            def predict(self, X):
                result = self.func(X, self.model)
                return result

##TODO write test cases, and determine best course of action for
class MonkeyModel(object):
        def __init__(self, model_name, path="./.models/"):
            directory = path+model_name          
            self.models = self._get_dependencies(file_type="model-object", 
                                                dependency_type="model_objects", 
                                                directory=directory)

            self.artifacts = self._get_dependencies(file_type="artifact", 
                                                dependency_type="artifacts", 
                                                directory=directory)

            self.func = pickle.load(open(directory+"/"+model_name+"-wrapper.pkl", 'rb'))
                
        def _get_dependencies(self, file_type, dependency_type, directory):
            dependencies = {}
            cnt = 0
            for f in listdir(directory):
                if isfile(join(directory, f)):
                    if file_type in f:
                        dependencies["{0}-{1}".format(file_type, cnt)] = pickle.load(open(directory+"/"+f, 'rb'))
                        cnt += 1
                    
            return dependencies

        def predict(self, X):
            return self.func(X, self.models, self.artifacts)
