# Remove hardcoded `sys.path` config

It is removed because:

- we use ".vscode/settings.json" to set Jupyter root
- we use "pyproject.toml" to treat letterboxd_data_pipeline as a Python package

## What is this hardcoded `sys.path` config?

A quick and dirty solution to import cross module solution for Jupyter notebook

- https://stackoverflow.com/a/35273613/7939633
- https://stackoverflow.com/a/44486700/7939633
