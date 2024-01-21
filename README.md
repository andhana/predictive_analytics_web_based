# predictive_analytics_web_based

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Inference](#inference)
- [Schedule Training](#schedule-training)
- [Documentation](#Documentation)
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/andhana/predictive_analytics_web_based.git

2. Install the reuquired Python libraries:

   ```bash
   pip install -r requirements.txt

## Usage

1. data-preparation
   
   The data_preparation.py script loads and prepares the dataset for training and inference.

   ```bash
   python data_preparation.py

This script reads customer interactions, purchase history, and product details data, merges them, and generates additional rows to reach a total of 1000 rows. The prepared data is saved in dataset/prepared_data.csv.

2. Model Training
   
   The training.py script trains a collaborative filtering model using the Surprise library.
   
   ```bash
   python training.py

This script uses the prepared data to train a collaborative filtering model, saves the trained model as model/recommendation_model_cf.joblib, and prints evaluation metrics.

3. Inference

   The inference.py script loads the trained model and provides recommendations for a given customer.

   ```bash
   python inference.py

This script takes a customer ID and the number of top recommendations as input and returns the recommended products.

4. Web Application

   The app.py script sets up a Flask web application for user interaction.
   
   ```bash
   python app.py

Open browser and type http://127.0.0.1:5000/. Input the customer ID, Number of Recommendation, then hit the Get Recommendation button for results.

## Schedule Training

The model is scheduled to be trained daily at midnight using the schedule library. The training is implemented in a separate thread to avoid blocking the main application.

## Documentation

1. data_preparation.py
   
   This script prepares the dataset for training and inference. It loads customer interactions, purchase history, and product details data, merges them, generates additional rows, and aggregates features.

2. training.py

   This script trains a collaborative filtering model using the Surprise library. It loads the prepared data, builds a training set, trains the model, saves the model, and evaluates its performance.

3. inference.py
   
   This script loads the trained collaborative filtering model and provides top product recommendations for a given customer ID.

4. app.py

   This script sets up a Flask web application for user interaction. It includes routes for inputting customer ID and receiving product recommendations. The application also schedules daily training of the recommendation model.
