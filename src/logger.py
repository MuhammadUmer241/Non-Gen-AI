import logging
import os
from datetime import datetime


Log_file= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log()"

project_root = os.path.dirname(os.getcwd())
log_path = os.path.join(project_root, "logs", Log_file)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH= os.path.join(log_path, Log_file)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= '[%(asctime)s ] %(lineno)d %(name)s- %(levelname)s %(message)s',
    level=logging.INFO,
)
