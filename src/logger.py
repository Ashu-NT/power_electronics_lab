import os
import logging
from datetime import datetime

BASE_DIR = os.getcwd()
LOG_FILE = f"{datetime.now().strftime('[%d_%m_%Y, %H_%M_%S]')}.log"

log_path = os.path.join(BASE_DIR,"logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
   
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    datefmt='%d-%m-%Y, %H:%M:%S',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
