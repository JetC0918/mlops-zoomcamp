## Experiment tracking

- Process of keeping track of all the **relevant information** from an **ML experiment**, including:
    - Source code
    - Environment
    - Data
    - Model
    - Hyperparameters
    - Metrics 

- Tracking is important to:
    - Reproducability
    - Organization
    - Optimization

#### ML Flow
- Open source platform for the machine learning lifecycle
- Contains 4 modules:
    1. Tracking
    2. Models
    3. Model Registry
    4. Projects

**Tracking experiments with ML Flow**
- MLflow Tracking allow organize experiment into multiple runs, and to keep track of:
    - Parameters
    - Metrics
    - Metadata
    - Artifacts
    - Models
- MLFlow automatically logs extra information about the run
    - Source code
    - Version of the code
    - Start and end time
    - Author

## MLFlow
#### Starting MLFlow
On CMD
```mlflow ui --backend-store-uri sqlite:///mlflow.db```

On Python
```
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("nyc-taxi")
```

#### Running MLFlow
Define a mlflow start run
```with mlflow.start_run():```

Logging the parameters
- Developer
```mlflow.set_tag("developer", "J")```
- Train data path
```mlflow.log_param("train-data-path", "./data/green_tripdata_2021-01.parquet")```
- Valid data path
```mlflow.log_param("valid-data-path", "./data/green_tripdata_2021-02.parquet")```
- Alpha
```mlflow.log_param("alpha", alpha)```
- Metrics - RSME
```mlflow.log_metric('rsme', rsme)```

Autologging the parameters
- Enable autologging before defining the variable X & Y
```
mlflow.xgboost.autolog()
x_train =
y_train = 

```

## Model Management 
**Logging Model**
- Log model as an artifact
```mlflow.log_artifact(local_path="models/lin_reg.bin", artifact_path="models_pickle") ```

- Log model using framework.log_model method
```mlflow.<framework>.log_model(booster, artifact_path="models_mlflow")```

**Load Models**
- As an general model object
```loaded_model = mlflow.pyfunc.load_model(logged_model)```

- As a framework model object
```xgboost_model = mlflow.xgboost.load_model(model_uri=logged_model)```

## Model Registry
- List of models that is production ready
- Some metrics to take note of:
    - Training Time
    - RSME
    - Size

**ML Client Class**
Import relevant packages
```
from mlflow.tracking import MlflowClient

MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"

client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
```
List the experiments
``` client.search_experiments() ```
View runs
```
from mlflow.entities import ViewType

runs = client.search_runs(
    experiment_ids='3',
    filter_string="metrics.rmse < 6.8",
    run_view_type=ViewType.ACTIVE_ONLY,
    max_results=5,
    order_by=["metrics.rmse ASC"]  
)
```
Register model
```mlflow.register_model(model_uri=model_uri, name="nyc-taxi-regressor")```
Update model description
```
client.update_model_version(
    name=model_name,
    version=model_version,
    description=f'The model version {model_version} was transisitioned to {new_stage} on {date}'
)
```