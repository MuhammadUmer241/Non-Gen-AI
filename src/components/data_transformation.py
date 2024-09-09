import os
import pandas as pd
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
            # target_col= ["y"]
            train_df_drop= train_df.drop("y",axis=1)
            test_df_drop= test_df.drop("y",axis=1)
            Ohe_col = ["education", "job", "previous_bins", "marital"]
            Ord_col = ["month", "default", "Some Loan", "contact"]
            Target_col = ["poutcome"]
            StandardScaler_col = ["duration", "cons_conf_idx", "nr_employed", "euribor3m", "cons_price_idx", "age"]
            Ordinal_Encoding = OrdinalEncoder(cols=Ord_col)
            # target_encoder = TargetEncoder(train_df["y"])
            ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
            SS = StandardScaler()


            CC = ColumnTransformer(
                transformers=[("OHE", ohe, Ohe_col),
                              # ("Target", target_encoder, Target_col),
                              ("Ordinal", Ordinal_Encoding, Ord_col),
                              ("Standardization", SS, StandardScaler_col)],
                remainder="passthrough"
            )
            pipeline = Pipeline(steps=[('preprocessor', CC)])
            train_df_transformed= pipeline.fit_transform(train_df_drop, train_df["y"])
            test_df_transformed= pipeline.transform(test_df_drop)
            logging.info("Pickle File")
            save_obj(
                self.preprocessor_path.data_preprocessor_path,
                pipeline
            )

            return (self.preprocessor_path.data_preprocessor_path,
                    pipeline)
        except Exception as e:
            Custom_Exception(e,sys)




