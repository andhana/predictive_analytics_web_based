import pandas as pd
import joblib
from surprise import KNNBasic, Reader, Dataset
from surprise.model_selection import cross_validate
from data_preparation import prepare_data

prepare_data()

def train_model():
    features = pd.read_csv('dataset/prepared_data.csv')

    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(features[['customer_id', 'page_views', 'time_spent']], reader)

    trainset = data.build_full_trainset()

    sim_options = {
        'name': 'cosine',
        'user_based': False
    }

    model = KNNBasic(sim_options=sim_options)
    model.fit(trainset)

    # Save the trained model
    joblib.dump(model, 'model/recommendation_model_cf.joblib')

    # evaluate the model
    cross_results = cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

    print(f"Mean RMSE: {cross_results['test_rmse'].mean()}")
    print(f"Mean MAE: {cross_results['test_mae'].mean()}")

if __name__ == "__main__":
    train_model()