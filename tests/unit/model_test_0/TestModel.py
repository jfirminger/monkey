class TestModel(object):

    def __init__(self):
        self.model = sum
        
    def predict(self, X):
        return {"results": self.model(X)}