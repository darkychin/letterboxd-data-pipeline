# Data Pipeline with Letterboxd Movies Data Set

A data pipeline demo using Kaggle data - Letterboxd Movies Dataset.

## How to run

### With Python

Prerequisite:

- uv

run entire end to end pipeline with comment below command

```bash
#  at directory /letterboxd-data-pipeline
uv run letterboxd_data_pipeline
```

## Data Source

- [letterbox movies data](https://www.kaggle.com/datasets/gsimonx37/letterboxd/data)

## Exploratory Data Analysis

See the Jupyter notebooks [here](./exploration).

## Data Tiers

For this project, we will use [medallion layer](https://www.databricks.com/glossary/medallion-architecture) as a template.

- External (/data/external) - raw and unmodified data from Kaggle
- Bronze (/data/bronze) - minimum modification and string conversion and save the final result as parquet
- Silver (/data/silver) - cleaned data with tranformed, standardized and schema applied data
- Gold (/data/gold) - aggregated data for dashboard usage

## Main Package

Majority of the pipeline code can be found [here](./letterboxd_data_pipeline).

## Current Progress

This is an ongoing project, and you can checkout the current progress with this [checklist](./docs/checklist.md).

## Future Plans

- Integrate with Github Actions
- Integrate with AWS Lambda with AWS SAM

## Other Reference Sources

- [Idea to set up a data pipeline project](https://www.reddit.com/r/dataengineering/comments/1j33t9e/comment/mfz8d0p/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
- [How to Test Lambda Functions Locally and Deploy to AWS using AWS SAM](https://www.youtube.com/watch?v=6hQ5pJ5xqkU)
- [Download Kaggle Datasets via API in Python](https://www.youtube.com/watch?v=hzcV0hDkfzs)
- https://stackoverflow.com/questions/55934733/documentation-for-kaggle-api-within-python
- https://technowhisp.com/kaggle-api-python-documentation/
- [file structure references](https://cookiecutter-data-science.drivendata.org/)
