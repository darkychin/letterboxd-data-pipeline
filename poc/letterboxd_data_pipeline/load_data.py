from os import listdir
import pandas as pd
from letterboxd_data_pipeline.constants import DATA_LAYER_PATH
from letterboxd_data_pipeline.data_layer import get_file_list

DIRECTORY = DATA_LAYER_PATH.get("external")


def get_local_raw_file_list():
    return [file for file in listdir(DIRECTORY)]


def load_local_data_single(file_name):
    df = {}
    df_name = file_name.split(".")[0]
    print(f"Loading: {file_name}")
    df[df_name] = pd.read_csv(f"{DIRECTORY}/{file_name}", dtype=str)
    print("Done!")
    return df


def load_local_data(file_list):
    df = {}
    print("Start loading data...")

    for file in file_list:
        df_name = file.split(".")[0]
        print(f"Loading: {file}")
        df[df_name] = pd.read_csv(f"{DIRECTORY}/{file}")
        print("Done!")
    print("Finish loading.")
    return df


def load_data_from_layer(layer: str, file_type="parquet"):
    (file_list, path) = get_file_list(layer)

    df: dict[str, pd.DataFrame | None] = {}
    print("Start loading data...")

    for file in file_list:
        df_name = file.split(".")[0]
        read_path = f"{path}/{file}"
        print(f"Loading: {read_path}")

        if file_type == "csv":
            df[df_name] = pd.read_csv(read_path)
        else:
            df[df_name] = pd.read_parquet(read_path)

        print("Done!")

    print("Finish loading.")
    return df


def load_files_from_layer(*, layer: str, file_list: list[str] = []):
    """
    Docstring for load_files_from_layer
    
    :param layer: data 
    :type layer: str
    :param file_list: Description
    :type file_list: list[str]
    
    * argument design reference: https://stackoverflow.com/a/75654179/7939633
    """
    (layer_file_list, path) = get_file_list(layer)

    target_file_list = []
    df: dict[str, pd.DataFrame | None] = {}

    if file_list:
        target_file_list = file_list
    else:
        target_file_list = layer_file_list

    print("Start loading data...")

    for file in target_file_list:
        """
        List of None concatenate to avoid:
        - IndexError: list index out of range (with file[1])
        - ValueError: not enough values to unpack (with unpack tuple)

        * reference: https://stackoverflow.com/a/21484229/7939633
        """
        # todo add file name clean up to avoid invalid naming for dataframe dictionary
        (df_name, file_type) = (file.split(".") + [None])[:2]

        read_path = f"{path}/{file}"
        print(f"Loading: {read_path}")

        if file_type == "csv":
            df[df_name] = pd.read_csv(read_path)
        else:
            df[df_name] = pd.read_parquet(read_path)

        print("Done!")

    print("Finish loading.")
    return df


# def __main__():
#     file_list = get_local_raw_file_list()

#     df = load_local_data(file_list=file_list)


# if __name__ == "__main__":
#     __main__()
