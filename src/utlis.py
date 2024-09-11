import os
import sys
import pickle

from src.logger import logging
from src.exception import Custom_Exception


def save_obj(pipeline_path, pipeline):
    try:
        # Assuming the Artifacts directory is at the same level as src
        artifacts_dir = os.path.dirname(os.path.dirname(os.getcwd()))
        file_path = os.path.join(artifacts_dir, pipeline_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            pickle.dump(pipeline, f)
        logging.info("Pickle file saved successfully!")

    except Exception as e:
        raise Custom_Exception(e, sys)


def open_pickle(file_path):
    with open(file_path, "rb") as file:
        OP = pickle.load(file)
        return OP

