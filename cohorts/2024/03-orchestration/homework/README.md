# Mage
- An open-source data pipeline tool for transforming and integrating data.

## Starting Mage
`docker-compose up`

## Running Mage
- Mage can be run at `http://127.0.0.1:6789/` or `http://localhost:6789/`

## Pipeline
- Contains blocks and code that want to run

## Blocks
- Maps an individual file in pipeline
- There are few types of blocks that used in this homework
  
#### Data Loader
- Block that is use to load data

#### Transformer
- Block that is used to transform the data
  
#### Data Exporter
- Block that is used to export the data

#### Pipeline used in homework
![image](/mlops/homework3/images/1.JPG)

- `Data_loader` block with file `data loader`
- The `Data_loader` block will load file and return a `df`
- First `Traansformer` block with `clean` file will clean the `df` from `Data_loader`
- Second `Transformer` block with `dv__model` file will fit a `dict vectorizer` and train a `Linear Regression` model
- `Data_exporter` with `export` file will register the model 
