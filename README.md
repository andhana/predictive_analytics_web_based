# Recommender System Web Based

This project aims to develop a recommendation system using collaborative filtering for recommending products to customers based on their behavior.

## Table of Contents

- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Inference](#inference)
- [Web Application](#web-application)
- [Documentation](#Documentation)
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/andhana/predictive_analytics_web_based.git

2. Install the reuquired Python libraries:

   ```bash
   pip install -r requirements.txt

## Tech Stack

**Languages:** python 3.7
**Machine Learning Algorithm:** Collaborative Filtering
**Web Framework:** Flask

## Usage
## Data Preparation

The data_preparation.py script loads and prepares the dataset for training and inference.

```bash
python data_preparation.py
```
This script reads customer interactions, purchase history, and product details data, merges them, and generates additional rows to reach a total of 1000 rows. The prepared data is saved in dataset/prepared_data.csv.

## Model Training

The training.py script trains a collaborative filtering model using the Surprise library.

```bash
python training.py
```
This script uses the prepared data to train a collaborative filtering model, saves the trained model as model/recommendation_model_cf.joblib, and prints evaluation metrics.
## Inference
## Web Application
## Documentation
