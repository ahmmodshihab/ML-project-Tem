import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

# অবজেক্ট (যেমন: মডেল বা প্রিপসেসর) সেভ করার ফাংশন
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

# সব অ্যালগরিদম ট্রেনিং এবং হাইপারপ্যারামিটার টিউনিং করার মূল ফাংশন
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            # GridSearchCV ব্যবহার করে বেস্ট প্যারামিটার খোঁজা
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            # বেস্ট প্যারামিটার দিয়ে মডেলকে আবার সেট করা
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # প্রেডিকশন এবং স্কোর ক্যালকুলেশন
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

# সেভ করা মডেল বা ফাইল লোড করার ফাংশন (প্রেডিকশন পাইপলাইনে লাগে)
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)