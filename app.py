from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# ১. হোম পেজ রুট
@app.route('/')
def index():
    return render_template('index.html') 

# ২. প্রেডিকশন রুট (যেখানে ফর্ম সাবমিট হবে)
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html') # ইউজার ইনপুট ফর্ম
    else:
        # ফর্ম থেকে ডেটা রিসিভ করা
        data = CustomData(
            gender=request.form.get('gender'),
            age=int(request.form.get('age')),
            salary=int(request.form.get('salary')),
            city=request.form.get('city')
        )

        # ডেটাকে ডেটাফ্রেমে রূপান্তর
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        # প্রেডিকশন পাইপলাইন কল করা
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # রেজাল্টটি ওয়েব পেজে পাঠানো
        return render_template('home.html', results=results[0])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)