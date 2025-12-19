## Kaggle
- importing `kaggle` will automatically read data from `os.environment`
  - `KAGGLE_USERNAME`
  - `KAGGLE_KEY`
- to use `kaggle.api.authenticate`, you must use the `kaggle.json` file, [source](https://technowhisp.com/kaggle-api-python-documentation/)
- default download path is `.cache/kagglehub/datasets` when no path is configured