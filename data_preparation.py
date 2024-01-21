import pandas as pd
import random
from datetime import datetime, timedelta

def prepare_data():
    # load and delimiter the data
    customer_interactions_data = pd.read_csv('dataset/customer_interactions.csv')
    purchase_history_data = pd.read_csv('dataset/purchase_history.csv', delimiter=';')
    product_details_data = pd.read_csv('dataset/product_details.csv', delimiter=';')

    # drop empty columns in purchase)history and product_details
    drop_empty_ph = purchase_history_data.columns[3:]
    drop_empty_pd = product_details_data.columns[4:]
    purchase_history = purchase_history_data.drop(columns=drop_empty_ph)
    product_details = product_details_data.drop(columns=drop_empty_pd)

    # merge the datasets
    merged_data = pd.merge(purchase_history, product_details, on="product_id")
    merged_data = pd.merge(merged_data, customer_interactions_data, on='customer_id')

    # generating addtional rows to 1000
    additional_rows = 9994
    additional_data = []
    for _ in range(additional_rows):
        category = random.choice(merged_data['category'])
        price_options = {
            'Electronics': [500, 800],
            'Clothing': [50],
            'Home & Kitchen': [200],
            'Beauty': [30]
        }[category]
        new_row = {
            "customer_id": random.choice(merged_data['customer_id']),
            "product_id": random.choice(merged_data['product_id']),
            "purchase_date": (datetime.strptime("2023-01-01", "%Y-%m-%d") + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
            "category": category,
            "price": random.choice(price_options),
            "ratings": round(random.uniform(1.0, 5.0)),
            "page_views": random.randint(10, 100),
            "time_spent": round(random.uniform(20, 150))
        }
        additional_data.append(new_row)
    
    # Concatenating the original data with additional rows
    df = pd.concat([merged_data, pd.DataFrame(additional_data)], ignore_index=True)
    
    # Aggregate the features
    features = df.groupby('customer_id').agg({
        'page_views': 'sum',
        'time_spent': 'sum',
        'price': 'mean',
        'ratings': 'mean',
    }).reset_index()
    
    return df, features

if __name__ == '__main__':
    df, features = prepare_data()
    df.to_csv('dataset/prepared_data.csv', index=False)
    print(df)
    