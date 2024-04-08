
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

path= os.getcwd()
def data_preprocessing():
    # Execute data pipeline (DAGs)
    print("Executing data pipeline (DAGs)...")
    classes = {'yes': 1, 'no': 0}
    X = []
    Y = []
    for i in classes:
        path = f'{path}/dataset/brain_tumor_dataset/' + i
        for j in os.listdir(path):
            img = cv2.imread(os.path.join(path, j), 0)
            img = cv2.resize(img, (240, 240), interpolation=cv2.INTER_CUBIC)
            X.append(img)
            Y.append(classes[i])
    x = np.array(X)
    y = np.array(Y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
    X_train = x_train.reshape(-1, 240, 240, 1)
    X_test = x_test.reshape(-1, 240, 240, 1)

    return X_train, X_test, y_train, y_test