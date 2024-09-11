import os
import pandas as pd
from Tools.scripts.generate_opcode_h import header
from sklearn.preprocessing import OneHotEncoder , TargetEncoder
from category_encoders import OrdinalEncoder
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import sys
from src.exception import Custom_Exception
from src.utlis import save_obj

from src.logger import logging

@dataclass
class data_tranformation_config:
    data_preprocessor_path= os.path.join("Artifacts", "preprocessor.pkl")


class data_transformation_initiate:
    def __init__(self):
        self.preprocessor_path= data_tranformation_config()

    def data_transformtion_init(self, train_path, test_path):

        try:
            train_df= pd.read_csv(train_path)
            test_df= pd.read_csv(test_path)
            Ohe_col = ["education", "job", "previous_bins", "marital"]
            Ord_col = ["month", "default", "Some Loan", "contact","poutcome"]
            StandardScaler_col = ["duration", "cons_conf_idx", "nr_employed", "euribor3m", "cons_price_idx", "age"]
            Ordinal_Encoding = OrdinalEncoder(cols=Ord_col)
            ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
            SS = StandardScaler()
            CC = ColumnTransformer(
                transformers=[("OHE", ohe, Ohe_col),
                              ("Ordinal", Ordinal_Encoding, Ord_col),
                              ("Standardization", SS, StandardScaler_col)],
                remainder="passthrough"
            )
            pipeline = Pipeline(steps=[('preprocessor', CC)])
            pipeline.fit(train_df[["age", "job", "marital", "education", "default", "Some Loan","month", "poutcome","contact",
           "cons_conf_idx", "euribor3m", "nr_employed","previous_bins","duration","cons_price_idx"]])
            logging.info("Pickle File")
            save_obj(
                self.preprocessor_path.data_preprocessor_path,
                pipeline
            )
            root_dir= os.path.dirname(os.path.dirname(os.getcwd()))
            pickle_file_path = os.path.join(root_dir, self.preprocessor_path.data_preprocessor_path)

            return pickle_file_path


        except Exception as e:
            Custom_Exception(e,sys)


