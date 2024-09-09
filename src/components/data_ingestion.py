import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import Custom_Exception
from dataclasses import dataclass
from src.components.data_transformation import data_transformation_initiate
from src.utlis import save_obj


@dataclass
class data_insgestion_config:
    train_path = os.path.join("Artifacts", "train.csv")
    test_path = os.path.join("Artifacts", "test.csv")
    raw_data = os.path.join("Artifacts", "data.csv")

class dataingestion:
    def __init__(self):
        self.path_ingestion= data_insgestion_config()

    def data_ingestion(self):
        try:
            logging.info("Read dataframe")

            current_dir = os.getcwd()

            # Construct the full path to the CSV file relative to the current working directory
            file_path = os.path.join(current_dir, "notebook", "data",
                                     "final_data.csv")
            df= pd.read_csv(file_path)
            root_dir = os.path.dirname(os.path.dirname(os.getcwd()))
            os.makedirs(os.path.join(root_dir, os.path.dirname(self.path_ingestion.raw_data)), exist_ok=True)
            df.to_csv(os.path.join(root_dir, self.path_ingestion.raw_data), index=False, header=True)
            logging.info("Enter Raw Data")

            logging.info("Train Test Initiate")
            train_set, test_set= train_test_split(df, test_size=0.3, random_state=42)
            train_set.to_csv(os.path.join(root_dir, self.path_ingestion.train_path), index=False, header=True)
            test_set.to_csv(os.path.join(root_dir, self.path_ingestion.test_path), index=False, header=True)




            return  (
                os.path.join(root_dir, self.path_ingestion.train_path),
                os.path.join(root_dir, self.path_ingestion.test_path)
            )
        except Exception as e:
            logging.info("data ingestion Error")
            Custom_Exception(e,sys)
if __name__== "__main__":
    obj= dataingestion()
    train_data_path , test_data_path = obj.data_ingestion()
    pipe= data_transformation_initiate()
    pipe.data_transformtion_init(train_data_path, test_data_path)
