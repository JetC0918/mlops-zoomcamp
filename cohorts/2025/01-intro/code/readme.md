## ML Ops - Week 1
#### 3 Stages of Machine Learning Project
1. Design
- Determine if Machine Learning is the right tool to solve the problem

2. Train
- Train the model and find the best possible model

3. Operate
- Deploy the model, customer can communicate with the model through API

#### Training a model
- Log all the models & parameters used to **experiment tracker**
- Model can be saved to **Model Registry** 

#### ML Pipelines
- A set of ML steps that can easily execute for different datasets & models
- EG: Load & Prepare data -> Vectorize -> Train

#### Model Deployment
- The trained model form ML Pipelines is deployed on Services for user to interact

#### Model Monitoring
- Monitor the performance of model, if there is drop in performance, retrain the model using ML Pipelines automation with/without human interaction

## MLOps maturity model
#### 0 - No MLOps
- Everything manually, nothing automated
- All code in Jupyter
- Good for POC project - experimenting project

#### 1 - DevOps, no MLOps
- Releases are automated
- Unit & Intergration Tests
- CI/CD
- OPS Metrics
- No experiment tracking
- No reproducability
- DS normally working alone
- POC ready for production

#### 2 - Automated Training
- Training pipeline
- Experiment tracking
- Model registry
- Low friction deployment
- DS work with engineer
- 2 - 3 + ML cases

#### 3 - Automated Deployment
- Easy to deploy model
- A/B test
- Monitoring
- 5 - 6+ ML cases / 1 very important case

#### 4 - Full MLOps Automation
- Everything automation