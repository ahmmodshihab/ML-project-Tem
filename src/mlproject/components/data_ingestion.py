import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# ১. কনফিগুরেশন ক্লাস (কোথায় ফাইল সেভ হবে তার পাথ ঠিক করা)
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# ২. মেইন ইনজেশন ক্লাস
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # ডেটা রিড করা (এখানে আপনার CSV পাথ দিন)
            df = pd.read_csv('notebook/data.csv') 
            
            # ফোল্ডার তৈরি করা (artifacts ফোল্ডার না থাকলে বানিয়ে নিবে)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Raw ডেটা সেভ করা
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            # ট্রেন-টেস্ট স্প্লিট
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # আলাদা আলাদা সেভ করা
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            print(f"Error occurred: {e}")

