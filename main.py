import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

if __name__ == "__main__":
    try:
        logging.info("মেইন পাইপলাইন শুরু হচ্ছে...")

        # ১. ডেটা ইনজেশন (Data Ingestion)
        # এটি CSV ফাইল পড়ে ট্রেন এবং টেস্ট সেটে ভাগ করবে
        ingestion = DataIngestion()
        train_data_path, test_data_path = ingestion.initiate_data_ingestion()
        logging.info("ডেটা ইনজেশন সফলভাবে সম্পন্ন হয়েছে।")

        # ২. ডেটা ট্রান্সফরমেশন (Data Transformation)
        # এটি ফিচার ইঞ্জিনিয়ারিং, স্কেলিং এবং এনকোডিং করবে
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )
        logging.info("ডেটা ট্রান্সফরমেশন (Scaling & Encoding) শেষ হয়েছে।")

        # ৩. মডেল ট্রেনিং (Model Trainer)
        # এটি একাধিক অ্যালগরিদম টেস্ট করবে এবং হাইপারপ্যারামিটার টিউন করে বেস্ট মডেলটি সেভ করবে
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        
        print(f"বেস্ট মডেলের R2 Score: {r2_score}")
        logging.info(f"মডেল ট্রেনিং সফল! স্কোর: {r2_score}")

    except Exception as e:
        logging.error("মেইন পাইপলাইনে সমস্যা হয়েছে!")
        raise CustomException(e, sys)