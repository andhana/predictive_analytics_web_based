# predictive_analytics_web_based

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Inference](#inference)
- [Web Application](#web-application)
- [Scheduled Training](#scheduled-training)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/andhana/predictive_analytics_web_based.git

2. Install the reuquired Python libraries:

   ```bash
   pip install -r requirements.txt

## Usage
1. Run app.py in terminal:
   
   ```bash
   python app.py
   Open browser and type http://127.0.0.1:5000/. Input the customer ID, Number of Recommendation, then hit the
   Get Recommendation button for results.

## Documentation

1. data_preparation.py
   
   This script prepares the dataset for training and inference. It loads customer interactions, purchase history, and product details data, merges them, generates additional rows, and aggregates features.

2. training.py
   
   This script trains a collaborative filtering model using the Surprise library. It loads the prepared data, builds a training set, trains the model, saves the model, and evaluates its performance.

3. inference.py
   
   This script loads the trained collaborative filtering model and provides top product recommendations for a given customer ID.

4. app.py
   This script sets up a Flask web application for user interaction. It includes routes for inputting customer ID and receiving product recommendations. The application also schedules daily training of the recommendation model.
