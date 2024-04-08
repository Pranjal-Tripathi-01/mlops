
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import json
import datetime
from logger_config import logger

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)
    
def data_preprocessing():
    try:
        getpath = os.getcwd()
        logger.info("Executing data preprocessing ...")
        classes = {'yes': 1, 'no': 0}
        X = []
        Y = []
        for i in classes:
            path = f'{getpath}/dags/dataset/brain_tumor_dataset/' + i
            for j in os.listdir(path):
                img = cv2.imread(os.path.join(path, j), 0)
                img = cv2.resize(img, (240, 240), interpolation=cv2.INTER_CUBIC)
                X.append(img.tolist())  
                Y.append(classes[i])
        x = np.array(X)
        y = np.array(Y)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
        X_train = x_train.reshape(-1, 240, 240, 1)
        X_test = x_test.reshape(-1, 240, 240, 1)
    except Exception as e:
        logger.error(f"Error in load data: {e}")
    logger.info("Data Preprocessing Completed")

    return {'X_train': X_train.tolist(),  
            'X_test': X_test.tolist(),  
            'y_train': y_train.tolist(),  
            'y_test': y_test.tolist()}  
