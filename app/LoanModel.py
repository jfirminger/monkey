import pandas as pd
import pickle

class LoanModel(object):

	def __init__(self):
		self.model = pickle.load(open('models/latePaymentsModel.pkl','rb'))
		
	def predict(self, X):
		df = pd.DataFrame.from_dict(X)
		scores = self.model.predict_proba(df)
		return {"results": scores.tolist()}