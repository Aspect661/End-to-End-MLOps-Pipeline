import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib
from src.datascience.utils.common import save_json 
from pathlib import Path

from src.datascience.entity.config_entity import ModelEvaluationConfig

import os

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/tuhindas01.official/datascienceproject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "tuhindas01.official"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "6943ca6113c81fe5a6832e4015e69217a193bf62"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):

        # Calculate evaluation metrics
        mse = mean_squared_error(actual, pred)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return mse, mae, r2

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(self.config.mlflow_uri).scheme

        with mlflow.start_run():

            predicted_quanlities = model.predict(X_test)
            (rmse, mae, r2) = self.eval_metrics(y_test, predicted_quanlities)

            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path = Path(self.config.metric_file_name), data = scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metrics({"rmse": rmse, "mae": mae, "r2": r2})

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")