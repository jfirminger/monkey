from os import listdir, remove, rmdir
from os.path import isfile, join, exists

def clean_up_dir(directory, path):
    for f in listdir(directory):
        f_path = join(directory, f)
        if isfile(f_path):
            remove(f_path) 
    rmdir(directory)
    rmdir(path)

class AddTwo():
        def __init__(self):
            pass
        def predict(self, X):
            return X+2

def test_easy_wrap_decorator(test_easy_wrap_local):
    at = AddTwo()
    
    path = "./.models/"
    model_name = "atmodel"
    directory = path+model_name

    easy_wrap = test_easy_wrap_local
    @easy_wrap(model_object=at, model_name=model_name, path=path)
    def invoke(X, model):
        return model.predict(X)

    assert bool(exists(directory+"/"+model_name+".pkl")) != False
    assert bool(exists(directory+"/"+model_name+"-wrapper.pkl")) != False

    clean_up_dir(directory, path)

def test_easy_class(test_easy_wrap_local, test_easy_model_class):
    at = AddTwo()
    
    path = "./.models/"
    model_name = "atmodel"
    directory = path+model_name

    easy_wrap = test_easy_wrap_local
    @easy_wrap(model_object=at, model_name=model_name, path=path)
    def invoke(X, model):
        return model.predict(X)

    easy_model = test_easy_model_class(model_name=model_name, path=path)
    assert easy_model.predict(1) == 3

    clean_up_dir(directory, path)