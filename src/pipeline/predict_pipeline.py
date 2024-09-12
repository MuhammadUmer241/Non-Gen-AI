import pickle

from src.exception import Custom_Exception
from src.utlis import open_pickle
import pandas as pd
import os
import sys
#
# with open(r"C:\Users\Umer\Desktop\Non Genrative AI\Artifacts\preprocessor.pkl", "rb") as f:
#     p= pickle.load(f)
#
# with open(r"C:\Users\Umer\Desktop\Non Genrative AI\Artifacts\model.pkl", "rb") as f:
#     m= pickle.load(f)
#
#
#
# list_ = ["age", "job", "marital", "education", "default", "Some Loan","month", "poutcome","contact",
#            "cons_conf_idx", "euribor3m", "nr_employed","previous_bins","duration","cons_price_idx","y"]
#
#
df= {"age": [14], "job":["self-employed"], "marital": ["single"],
     "education": ["university.degree"], "default":["no"], "Some Loan":["no"], "month":["jul"],
     "poutcome": ["nonexistent"], "contact":["telephone"], "cons_conf_idx": [32], "euribor3m":[1.3], "nr_employed":[4355],
     "previous_bins":["New Client"], "duration":[324], "cons_price_idx":[32]}

df_ =pd.DataFrame(df)
# print(df_.columns)
#
# df_new= p.transform(df_)
# y=m.predict(df_new)
# print(y)

class predict_by_post:
    def predict(self , ddf):
        try:

            root = os.path.dirname(os.path.dirname(os.getcwd()))
            folder= os.path.join(root, "Artifacts")
            preprocessor = open_pickle(os.path.join(folder, "preprocessor.pkl"))
            model= open_pickle(os.path.join(folder, "model.pkl"))
            ddf_ = preprocessor.transform(ddf)
            y= model.predict(ddf_)
            return y
        except  Exception as e:
            Custom_Exception(e, sys)




