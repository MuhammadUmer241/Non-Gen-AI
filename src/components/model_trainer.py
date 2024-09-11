import os.path
import pickle
import pandas as pd
import xgboost as xgb
from pandas.core.common import random_state
from pandas.io.formats.printing import pprint_thing
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from dataclasses import dataclass
from src.logger import logging
from src.utlis import save_obj
from src.components.data_transformation import data_transformation_initiate
from sklearn.metrics import accuracy_score
@dataclass
class model_trainer_config:
    model_trainer_path= os.path.join("Artifacts", "model.pkl")

class model_trainer:
    def __init__(self):
        self.model_path= model_trainer_config()
    def model_trainer_initate(self, train_path:str ,  test_path:str, preprocessor_path:str, models:list):
        """
        This method make a pickle file in Artifacts and train the given model
        :param train_path:
        :param test_path:
        :param preprocessor_path:
        :param models:
        :return: path of pickle model
        """
        train_df= pd.read_csv(train_path)
        # print(train_df.columns)
        list_ = ["age", "job", "marital", "education", "default", "Some Loan","month", "poutcome","contact",
           "cons_conf_idx", "euribor3m", "nr_employed","previous_bins","duration","cons_price_idx","y"]
        train_df= train_df[list_]
        test_df= pd.read_csv(test_path)
        test_df= test_df[list_]
        y_train= train_df["y"]
        y_test= test_df["y"]
        train_df_drop= train_df.drop("y",axis=1)
        test_df_drop = test_df.drop("y",axis=1)

        with open(preprocessor_path,"rb") as f:
            preprocesor =  pickle.load(f)
        X_train_Drop = preprocesor.fit_transform(train_df_drop)
        X_test_Drop = preprocesor.transform(test_df_drop)
        X_train_transformed_df = pd.DataFrame(X_train_Drop, columns=preprocesor.get_feature_names_out())
        X_test_transformed_df = pd.DataFrame(X_test_Drop, columns=preprocesor.get_feature_names_out())

        models.fit(X_train_transformed_df, y_train)
        y_pred = models.predict(X_test_transformed_df)
        score= accuracy_score(y_test,y_pred)
        print("accuracy score:", score)
        save_obj(
            self.model_path.model_trainer_path,
            models,
        )
        root_dir = os.path.dirname(os.path.dirname(os.getcwd()))
        pickle_file_path = os.path.join(root_dir, self.model_path.model_trainer_path)
        return pickle_file_path




