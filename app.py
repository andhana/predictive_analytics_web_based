from flask import Flask, render_template, request
from data_preparation import prepare_data
from inference import load_and_predict_model
import pandas as pd
import joblib
import schedule
import threading
import time
from training import train_model

# Function to train the model
def scheduled_train():
    while True:
        print("Training started at", time.strftime("%Y-%m-%d %H:%M:%S"))
        train_model()
        print("Training completed at", time.strftime("%Y-%m-%d %H:%M:%S"))

        now = time.localtime()
        next_training = time.mktime((now.tm_year, now.tm_mon, now.tm_mday + 1, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
        sleep_time = next_training - time.time()
        time.sleep(sleep_time)

# schedule training in every 00:00 AM
schedule.every().day.at("00:00").do(train_model)

# start scheduling thread
schedule_thread = threading.Thread(target=scheduled_train)
schedule_thread.start()

df, features = prepare_data()
model = joblib.load('model/recommendation_model_cf.joblib')

app = Flask(__name__)

# function to load and predict
def make_recommendations(customer_id, top_n):
    return load_and_predict_model('model/recommendation_model_cf.joblib', 'dataset/prepared_data.csv', customer_id, top_n)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        customer_id = request.form['customer_id']
        top_n = int(request.form['top_n'])

        # check if the customer ID exists in the dataset
        if int(customer_id) not in features['customer_id'].unique():
            return render_template('error.html', error=f"Customer ID '{customer_id}' does not exist.")

        # make predictions using inference function
        recommended_products = make_recommendations(customer_id, top_n)

        return render_template('result.html', customer_id=customer_id, recommended_products=recommended_products)
    
    except Exception as e:
        return render_template('error.html', error=str(e))
    
if __name__ == '__main__':
    app.run(debug=True)