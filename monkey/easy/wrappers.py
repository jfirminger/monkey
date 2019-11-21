import dill as pickle

class EasyModel(object):
            def __init__(self, model_name, path="./.models/"):
                directory = path+model_name
                self.model = pickle.load(open(directory+"/"+model_name+".pkl", 'rb'))
                self.func = pickle.load(open(directory+"/"+model_name+"-wrapper.pkl", 'rb'))
            def predict(self, X):
                result = self.func(X, self.model)
                return result



