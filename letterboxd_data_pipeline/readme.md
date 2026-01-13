## Version
- Python 3.14.0

## How to run
1. go to directory ["./letterboxd_data_pipeline"](./letterboxd_data_pipeline/)
2. run command `python .`

## ELT flow
- extract csv data from Kaggle
- load data as python pandas dataframe and save it
- transform data
- aggregate data

Note

Each data steps need to be saved locally so we can start from which ever checkpoints we want to.