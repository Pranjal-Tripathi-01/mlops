import os
from logger_config import logger

def load_data():
    try:
        getpath= os.getcwd()
        logger.info("Accessing and loading data ...")
        path_to_folder = f"{getpath}/dataset/brain_tumor_dataset"
        no_tumor_img = os.listdir(path=os.path.join(path_to_folder, 'no'))
        yes_tumor_img = os.listdir(path=os.path.join(path_to_folder, 'yes'))
    except Exception as e:
        logger.error(f"Error in load data: {e}")

    logger.info("Data loading completed")