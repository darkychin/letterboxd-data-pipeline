## Kaggle

- importing `kaggle` will automatically read data from `os.environment`
  - `KAGGLE_USERNAME`
  - `KAGGLE_KEY`
- to use `kaggle.api.authenticate`, you must use the `kaggle.json` file, [source](https://technowhisp.com/kaggle-api-python-documentation/)
- default download path is `.cache/kagglehub/datasets` when no path is configured

## File Type

- "movies.csv" vs "movies.parquet", parquet is around 32% smaller

## Data Cleaning

### Missing Values

[Types of missing values](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/)

- Missing Completely At Random (MCAR)
- Missing At Random (MAR)
- Missing Not At Random (MNAR)

#### Methods

- [Listwise and Pairwise deletion](https://www.statisticssolutions.com/missing-data-listwise-vs-pairwise/)
- Imputation
  - Mode, Median or Mean[[source](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/)]
  - Backward or forward fill [[source](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/)]
- "Missingness" as a feature [[source](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/)]
- Advanced algorithm
  - KNN [[source](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/)]
  - interpolation

## How to utilize parquet

https://medium.com/munchy-bytes/are-you-using-parquet-with-pandas-in-the-right-way-595c9ee7112
