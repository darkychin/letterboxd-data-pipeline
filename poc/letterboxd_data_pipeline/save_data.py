import pandas as pd
from letterboxd_data_pipeline.utils import make_data_path
from letterboxd_data_pipeline.constants import DATA_LAYER_PATH
from letterboxd_data_pipeline.data_layer import get_file_path


def save_df(*, df: pd.DataFrame, layer: str, df_name: str):
    if not df_name:
        raise Exception("Dataframe name cannot be empty!")

    file_path = get_file_path(layer)
    save_path = f"{file_path}/{df_name}"

    make_data_path(file_path)

    print(f"Saving dataframe {df_name} into {file_path}")
    df.to_parquet(save_path)
    print("Complete!")


def save_all_data(df_dict: dict[str, pd.DataFrame], layer: str):
    file_path = get_file_path(layer)

    make_data_path(file_path)

    print("Start saving data...")

    for df_name in df_dict:
        df = df_dict[df_name]
        save_df(df=df, layer=layer, df_name=df_name)
