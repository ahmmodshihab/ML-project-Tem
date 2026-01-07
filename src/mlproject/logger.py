import logging
import os
from datetime import datetime

# 2 works 1) file name create   2) log folder create   3) 2 ta k join kore dea

# ফাইলের নাম নির্ধারণ
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 

# ১.শুধু ফোল্ডারের পাথ তৈরি করা
log_path=os.path.join(os.getcwd(),"logs")  # log file er path,log folderr banate argument

#২.শুধুমাত্র ফোল্ডারটি তৈরি করা (ফাইলের নাম ছাড়া)
os.makedirs(log_path,exist_ok=True) # making log folder

#৩.ফোল্ডারের ভেতরে ফাইলের পূর্ণ ঠিকানা তৈরি করা
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

#এই অংশটিই ঠিক করে লগ ফাইলটি দেখতে কেমন হবে:
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
