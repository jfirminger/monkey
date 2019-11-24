import dill as pickle
import os

def easy_wrap(model_object, model_name, path=".models/"):
    def model_wrapper(func):
        directory = path+model_name
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            pickle.dump(model_object, open(directory+"/"+model_name+".pkl", 'wb'))
        except Exception as e:
            print(e)
            print("Cannot save local model_object {}. Try defining as global variable".format(model_object))
        try:
            pickle.dump(func, open(directory+"/"+model_name+"-wrapper.pkl", 'wb'))
        except Exception as e:
            print(e)
            print("Cannot save local func {}. Try defining as global variable".format(func))        
        return func
    return model_wrapper

def monkey_wrap(model_objects, artifacts, model_name, path=".models/"):
    def model_wrapper(func):
        directory = path+model_name
        if not os.path.exists(directory):
            os.makedirs(directory)

        for i, model in enumerate(model_objects):
            try:
                pickle.dump(model, open(directory+"/"+model_name+"-model-object-{}.pkl".format(i), 'wb'))
            except Exception as e:
                print(e)
                print("Cannot save local model_object {}. Try defining as global variable".format(model))

        for i, artifact in enumerate(artifacts):
            try:
                pickle.dump(artifact, open(directory+"/"+model_name+"-artifact-{}.pkl".format(i), 'wb'))
            except Exception as e:
                print(e)
                print("Cannot save local artifact_object {}. Try defining as global variable".format(artifact))
        
        try:
            pickle.dump(func, open(directory+"/"+model_name+"-wrapper.pkl", 'wb'))
        except Exception as e:
            print(e)
            print("Cannot save local func {}. Try defining as global variable".format(func))
        return func
    return model_wrapper