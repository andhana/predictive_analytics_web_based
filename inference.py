import pandas as pd
from surprise import Dataset, Reader
import joblib

def load_and_predict_model(model_path, features_path, customer_id, top_n=5):
    # load the data
    features = pd.read_csv(features_path)

    # check if the customer ID exists in the dataset
    if int(customer_id) not in features['customer_id'].unique():
        print(f"Customer ID '{customer_id}' does not exist.")
        return None

    # load model, collaborative filtering
    model = joblib.load(model_path)

    # extract product IDs from the product details
    # unique_pids = features['product_id'].unique()
    unique_pids = features[~((features['customer_id'] == int(customer_id)) & (features['page_views'] > 0))]['product_id'].unique()
    # build the testset
    # testset = [(customer_id, product_id, 3) for product_id in unique_pids]
    predictions = [(customer_id, product_id, model.predict(customer_id, product_id).est) for product_id in unique_pids]

    # make predictions
    # predictions = model.test(testset)

    # extract the top N recommended products
    unique_recommendations = set()
    recommended_products = []
    for pred in sorted(predictions, key=lambda x: x[2], reverse=True):
        if len(unique_recommendations) >= top_n:
            break

        product_info = features[features['product_id'] == pred[1]].iloc[0]
        recommendation = (
            product_info['product_id'],
            product_info['category'],
            product_info['price']
        )

        if recommendation not in unique_recommendations:
            unique_recommendations.add(recommendation)
            recommended_products.append({
                'product_id': recommendation[0],
                'category': recommendation[1],
                'price': recommendation[2]
            })

    while len(recommended_products) < top_n:
        recommended_products += recommended_products
    recommended_products = recommended_products[:top_n]

    return recommended_products

if __name__ == "__main__":
    model_path = 'model/recommendation_model_cf.joblib'
    features_path = 'dataset/prepared_data.csv'
    customer_id = input("Enter customer ID: ")
    top_n = int(input("Enter the number of recommendations product: "))

    predictions = load_and_predict_model(model_path, features_path, customer_id, top_n)

    if predictions:
        print(f"\nTop {top_n} recommended products for Customer ID {customer_id}:")
        for product in predictions:
            print(f"Product ID: {product['product_id']}, Category: {product['category']}, Price: {product['price']}")
