import dill as pickle
import os

def easy_wrap(model_object, model_name, path="./.models/"):
    def model_wrapper(func):
        directory = path+model_name
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            pickle.dump(model_object, open(directory+"/"+model_name+".pkl", 'wb'))
            pickle.dump(func, open(directory+"/"+model_name+"-wrapper.pkl", 'wb'))
        except Exception as e:
            print(e)
            print("Cannot save local model_object {}. Try defining as global variable".format(model_object))
        return func
    return model_wrapper