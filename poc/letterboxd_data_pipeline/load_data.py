from os import listdir
import pandas as pd
from .constants import DATA_LAYER_PATH
from .data_layer import get_file_list

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


# def __main__():
#     file_list = get_local_raw_file_list()

#     df = load_local_data(file_list=file_list)


# if __name__ == "__main__":
#     __main__()
