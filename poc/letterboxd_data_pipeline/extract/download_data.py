from kaggle import api as kaggle_api
from letterboxd_data_pipeline.constants import KAGGLE_DATA, DATA_LAYER_PATH
from letterboxd_data_pipeline.utils import make_data_path

DATA_SOURCE = KAGGLE_DATA.get("source")
EXTERNAL_DATA_PATH = DATA_LAYER_PATH.get("external")


def get_target_files(file_list: list):
    """
    Cherry pick none `poster` file
    """
    target_file_list = [file.name for file in file_list if "poster" not in file.name]
    return target_file_list


def start():
    """
    Start load data
    """
    make_data_path(EXTERNAL_DATA_PATH)

    target_file_list = get_target_files(
        kaggle_api.dataset_list_files(DATA_SOURCE).files
    )

    print("Try to download data")
    print("...")
    try:
        # kaggle_api.dataset_download_files(
        #     source_path, path=external_data_destination, unzip=True, quiet=False
        # )
        kaggle_api.dataset_download_files(
            DATA_SOURCE, path=EXTERNAL_DATA_PATH, unzip=True, quiet=False
        )
        # todo use dataset_download_file instead to avoid downloading poster and their related data, then do unzipping
    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("Download successful!")
        return target_file_list


def __main__():
    start()


if __name__ == "__main__":
    __main__()


# References
# - Kaggle download data sets to target path: https://stackoverflow.com/a/54869077/7939633
# - Kaggle missing API documentation: https://technowhisp.com/kaggle-api-python-documentation/
