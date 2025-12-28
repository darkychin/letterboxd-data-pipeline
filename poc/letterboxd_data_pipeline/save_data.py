import pandas as pd
from letterboxd_data_pipeline.utils import make_data_path
from letterboxd_data_pipeline.constants import DATA_LAYER_PATH


def save_all_data(dataframes: dict[str, pd.DataFrame], layer: str):
    if layer not in DATA_LAYER_PATH:
        raise Exception("Invalid data source path!")

    file_path = DATA_LAYER_PATH.get(layer)

    make_data_path(file_path)

    print("Start saving data...")

    for df_name in dataframes:
        df = dataframes[df_name]
        print(f"Saving {df_name} into {file_path}")
        df.to_parquet(f"{file_path}/{df_name}")
        print("Complete!")
