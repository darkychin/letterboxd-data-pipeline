import os
from kaggle import api as kaggle_api

#  todo use contants file instead

source_path = "gsimonx37/letterboxd"
# source_path2 = "wardabilal/spotify-global-music-dataset-20092025"
data_destination = "./data"
external_data_destination = data_destination + "/external"


def get_target_files(file_list: list):
    """
    Cherry pick none `poster` file
    """
    target_file_list = (file.name for file in file_list if "poster" not in file.name)
    return target_file_list


def make_data_path():
    """
    Make `./data/raw` path
    """
    if not os.path.exists(external_data_destination):
        print("Creating data directory")
        os.makedirs(external_data_destination)


def start():
    """
    Start load data
    """
    make_data_path()

    print("Try to download data")
    print("...")
    try:
        kaggle_api.dataset_download_files(
            source_path, path=external_data_destination, unzip=True, quiet=False
        )
        # todo use dataset_download_file instead, then do unzipping
    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("Download successful!")
        return get_target_files()


# References
# - Kaggle download data sets to target path: https://stackoverflow.com/a/54869077/7939633
# - Kaggle missing API documentation: https://technowhisp.com/kaggle-api-python-documentation/
