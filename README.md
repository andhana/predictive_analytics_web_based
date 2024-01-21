# predictive_analytics_web_based

recommendation_system/
│
├── dataset/
│   ├── customer_interactions.csv
│   ├── purchase_history.csv
│   ├── product_details.csv
│   └── prepared_data.csv
│
├── model/
│   └── recommendation_model_cf.joblib
│
├── templates/
│   ├── error.html
│   ├── index.html
│   └── result.html
│
├── app.py
├── data_preparation.py
├── inference.py
├── README.md
├── requirements.txt
└── training.py


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
1. Data Preparation:
   The data_preparation.py script loads and prepares the dataset for training and inference.

   ```bash
   python data_preparation.py
