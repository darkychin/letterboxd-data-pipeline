KAGGLE_DATA = {
    "source": "gsimonx37/letterboxd",
    # smaller data source for testing only
    # "source": "wardabilal/spotify-global-music-dataset-20092025",
}

# medallion layer: https://www.databricks.com/glossary/medallion-architecture
DATA_LAYER_PATH = {
    "root": "../data",
    "external": "../data/external",
    "bronze": "../data/bronze",
    "silver": "../data/silver",
    "gold": "../data/gold",
}

# reference: https://stackoverflow.com/a/59802500/7939633
POSSIBLE_NA_LIST = ["na", "null", "nan", "none"]
