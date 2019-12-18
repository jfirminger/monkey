from os import listdir, remove, rmdir
from os.path import isfile, join, exists
import shutil

def clean_up_dir(directory):
    shutil.rmtree(directory)

class AddTwo():
        def __init__(self):
            pass
        def predict(self, X):
            return X+2

class AddThree():
        def __init__(self):
            pass
        def predict(self, X):
            return X+3

def test_easy_wrap_decorator_local(test_easy_wrap_local):
    at = AddTwo()
    
    path = ".models/"
    model_name = "atmodel"
    directory = path+model_name

    easy_wrap = test_easy_wrap_local
    @easy_wrap(model_object=at, model_name=model_name, path=path)
    def invoke(X, model):
        return model.predict(X)

    assert bool(exists(directory+"/"+model_name+"-model-object.pkl")) != False
    assert bool(exists(directory+"/"+model_name+"-wrapper.pkl")) != False
    
    clean_up_dir(path)

def test_monkey_wrap_decorator_local(test_monkey_wrap_local):
    a2 = AddTwo()
    a3 = AddThree()

    v = {"run":"sure"}

    path = ".models/"
    model_name = "addmodel"
    directory = path+model_name

    monkey_wrap = test_monkey_wrap_local
    @monkey_wrap([a2, a3], [v], model_name=model_name)
    def invoke(X, models, artifacts):
        a2 = models["model-0"]
        a3 = models["model-1"]

        v = artifacts["artifact-0"]

        if v["run"] == "sure":
            return a2(0)+a3(0)

    assert bool(exists(directory+"/"+model_name+"-model-object-0.pkl")) != False
    assert bool(exists(directory+"/"+model_name+"-model-object-1.pkl")) != False
    assert bool(exists(directory+"/"+model_name+"-artifact-0.pkl")) != False

    clean_up_dir(path)

def test_easy_class_local(test_easy_wrap_local, test_easy_model_class):
    at = AddTwo()
    
    path = ".models/"
    model_name = "atmodel"

    easy_wrap = test_easy_wrap_local
    @easy_wrap(model_object=at, model_name=model_name, path=path)
    def invoke(X, model):
        return model.predict(X)

    easy_model = test_easy_model_class(model_name=model_name, path=path)
    assert easy_model.predict(1) == 3

    clean_up_dir(path)


def test_monkey_class_local(test_monkey_wrap_local, test_monkey_model_class):
    a2 = AddTwo()
    a3 = AddThree()

    v = {"run":"sure"}

    path = ".models/"
    model_name = "addmodel"

    monkey_wrap = test_monkey_wrap_local
    @monkey_wrap([a2, a3], [v], model_name=model_name, path=path)
    def invoke(X, models, artifacts):
        print(models)
        print(artifacts)
        a2 = models["model-object-0"]
        a3 = models["model-object-1"]

        v = artifacts["artifact-0"]

        print(a2)
        print(a3)

        if v["run"] == "sure":
            return a2.predict(0)+a3.predict(0)

    monkey_model = test_monkey_model_class(model_name=model_name, path=path)
    assert monkey_model.predict(0) == 5

    clean_up_dir(path)

