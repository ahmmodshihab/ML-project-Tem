import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import save_object
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_transformer_object(self):
        # আপনার ডেটাসেট অনুযায়ী কলামের নাম দিন
        numerical_columns = ["age", "salary"] 
        categorical_columns = ["gender", "city"]

        num_pipeline = Pipeline(steps=[("scaler", StandardScaler())])
        cat_pipeline = Pipeline(steps=[("one_hot_encoder", OneHotEncoder())])

        preprocessor = ColumnTransformer([
            ("num_pipeline", num_pipeline, numerical_columns),
            ("cat_pipeline", cat_pipeline, categorical_columns)
        ])
        return preprocessor

    def initiate_data_transformation(self, train_path, test_path):
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        preprocessing_obj = self.get_transformer_object()

        target_column_name = "target_column" # আপনার টার্গেট কলামের নাম দিন

        input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
        target_feature_train_df = train_df[target_column_name]

        input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
        target_feature_test_df = test_df[target_column_name]

        # ট্রান্সফর্মেশন অ্যাপ্লাই করা
        train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
        test_arr = preprocessing_obj.transform(input_feature_test_df)

        # ফিচার এবং টার্গেট একসাথে জোড়া লাগানো
        train_arr = np.c_[train_arr, np.array(target_feature_train_df)]
        test_arr = np.c_[test_arr, np.array(target_feature_test_df)]

        # প্রিপসেসর সেভ করা (ভবিষ্যতে প্রেডিকশনের জন্য লাগবে)
        save_object(self.data_transformation_config.preprocessor_obj_file_path, preprocessing_obj)

        return train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path