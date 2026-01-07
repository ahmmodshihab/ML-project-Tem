import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object # utils-এ একটি load_object ফাংশন থাকতে হবে
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # ট্রেইন করার সময় যে মডেল আর প্রিপসেসর সেভ করেছিলেন তার পাথ
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            # মডেল এবং প্রিপসেসর লোড করা
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # নতুন ডেটাকে স্কেলিং/প্রি-প্রসেস করা
            data_scaled = preprocessor.transform(features)
            
            # প্রেডিকশন বের করা
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

# এই ক্লাসটি ইউজার ইনপুটকে একটি DataFrame-এ কনভার্ট করবে
class CustomData:
    def __init__(self, gender: str, age: int, salary: int, city: str):
        self.gender = gender
        self.age = age
        self.salary = salary
        self.city = city

    def get_data_as_data_frame(self):
        try:
            # ইউজারের দেওয়া ডেটাকে ডিকশনারি আকারে সাজানো
            custom_data_input_dict = {
                "gender": [self.gender],
                "age": [self.age],
                "salary": [self.salary],
                "city": [self.city],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)