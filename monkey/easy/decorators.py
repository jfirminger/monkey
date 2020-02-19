import dill as pickle
import torch.nn as nn
from monkey.easy.frameworks import save_pytorch_model
from monkey.easy.utils import MonkeyLog
import os
from os.path import join


def easy_wrap(model_object, model_name, path=".models"):
    def model_wrapper(func):
        directory = join(path, model_name)
        monkey_log = MonkeyLog(
                                directory=directory, 
                                log_type="easy_wrap")
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            if isinstance(model_object, nn.Module):
                model_path = model_name+"-pytorch-model-object.pt"
                save_pytorch_model(model_object, join(directory, model_path))
                monkey_log.add_model(model_path, "pytorch")
            else:
                model_path = model_name+"-model-object.pkl"
                pickle.dump(model_object, open(join(directory, model_path), 'wb'))
                monkey_log.add_model(model_path, "pickle")
        except Exception as e:
            print(e)
            print("Cannot save local model_object {}. Try defining as global variable".format(model_object))
        try:
            func_path = model_name+"-wrapper.pkl"
            pickle.dump(func, open(join(directory, func_path), 'wb'))
            monkey_log.add_wrapper(func_path)
        except Exception as e:
            print(e)
            print("Cannot save local func {}. Try defining as global variable".format(func))  
        monkey_log.save_log()      
        return func
    return model_wrapper

def monkey_wrap(model_objects, artifacts, model_name, path=".models"):
    def model_wrapper(func):
        directory = join(path, model_name)
        if not os.path.exists(directory):
            os.makedirs(directory)

        for i, model_object in enumerate(model_objects):
            try:
                if isinstance(model_object, nn.Module):
                    save_pytorch_model(model_object, directory+"/"+model_name+"-pytorch-model-object-{}.pt".format(i))
                else:
                    pickle.dump(model_object, open(directory+"/"+model_name+"-model-object-{}.pkl".format(i), 'wb'))
            except Exception as e:
                print(e)
                print("Cannot save local model_object {}. Try defining as global variable".format(model_object))

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