import os
import pickle
import click
import mlflow
import mlflow.sklearn

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports DictVectorizer artifact and linear regression model using MLFlow
    """
    # Unpack the data
    dv , lr = data

    # Set tracking uri
    mlflow.set_tracking_uri("http://mlflow:5000")

    with mlflow.start_run() as run:
        # Log the model
        mlflow.sklearn.log_model(lr, 'Linear Regreession Model')

        # Save Dictvectorizer artifact
        dv_path = 'dict_vectorizer.pkl'
        with open(dv_path, 'wb') as f:
            pickle.dump(dv, f)
        
        # Log the artifact
        mlflow.log_artifact(dv_path, artifact_path ="dict_vectorizer")

        run_id = run.info.run_id

    # Register the model 
    model_uri = f"runs:/{run_id}/model"
    mlflow.register_model(model_uri=model_uri,name='taxi-model')