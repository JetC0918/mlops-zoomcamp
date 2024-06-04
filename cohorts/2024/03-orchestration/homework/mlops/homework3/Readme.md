## Question 1. Run Mage
First, let's run Mage with Docker Compose. Follow the quick start guideline.

What's the version of Mage we run?
![image](/cohorts/2024/03-orchestration/homework/mlops/homework3/images/01.png)
- v0.9.70
  
## Question 2. Creating a project
Now let's create a new project. We can call it `homework_03`, for example.

How many lines are in the created metadata.yaml file?
![image](/cohorts/2024/03-orchestration/homework/mlops/homework3/images/02.png)
- 55 Lines

  
## Question 3. Creating a pipeline
Let's create an ingestion code block.

In this block, we will read the March 2023 Yellow taxi trips data.

How many records did we load?
![image](/cohorts/2024/03-orchestration/homework/mlops/homework3/images/03.png)
- 3,403,766

  
## Question 4. Data preparation
Let's use the same logic for preparing the data we used previously. We will need to create a transformer code block and put this code there.

This is what we used (adjusted for yellow dataset):

```
def read_dataframe(filename):
    df = pd.read_parquet(filename)

    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df.duration = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)]

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)
    
    return df
```
Let's adjust it and apply to the data we loaded in question 3.

What's the size of the result?
![image](/cohorts/2024/03-orchestration/homework/mlops/homework3/images/04.png)
- 3,316,216
  
## Question 5. Train a model
We will now train a linear regression model using the same code as in homework 1

Fit a dict vectorizer Train a linear regression with default parameres Use pick up and drop off locations separately, don't create a combination feature Let's now use it in the pipeline. We will need to create another transformation block, and return both the dict vectorizer and the model

What's the intercept of the model?

Hint: print the intercept_ field in the code block
![image](/cohorts/2024/03-orchestration/homework/mlops/homework3/images/05.png)
- 24.77

## Question 6. Register the model
The model is trained, so let's save it with MLFlow.

Find the logged model, and find MLModel file. What's the size of the model? (model_size_bytes field):
![image](/cohorts/2024/03-orchestration/homework/mlops/homework3/images/06.png)
- 4,534
