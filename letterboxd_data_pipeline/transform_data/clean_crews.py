import pandas as pd
from letterboxd_data_pipeline.save_data import save_df

# todo refactor to a more friendly single file loading
from letterboxd_data_pipeline.load_data import load_files_from_layer
from letterboxd_data_pipeline.constants import DATA_LAYER_PATH
from letterboxd_data_pipeline.transform_data.clean_common import process_duplicates
from letterboxd_data_pipeline.transform_data.schema import SILVER_SCHEMA
from letterboxd_data_pipeline.explore_data import is_possible_na

df_name = "crews"
clean_df_name = f"clean_{df_name}"
file_name = f"{df_name}.parquet"
source_path = DATA_LAYER_PATH.get("bronze")
destination_path = DATA_LAYER_PATH.get("silver")
destination_layer = "silver"


def format_column_role(series: pd.Series):
    # print(series.str.contains(r"[^\w ]")).sum())
    # Results: contain "co-director" only, which is permitted

    new_series = series.str.lower().str.strip()

    print('Transform column "role" complete!')
    return new_series


def format_column_name(series: pd.Series):
    new_series = series.copy(True)

    print("Transform nameless crew member")
    nameless_placeholder = "Nameless"
    new_series.loc[is_possible_na(new_series)] = nameless_placeholder
    new_series = new_series.fillna(nameless_placeholder)

    print("Remove whitespace except space")
    new_series = new_series.str.strip()  # remove front and trailing whitespace
    # reference https://stackoverflow.com/a/4903946/7939633
    new_series.replace(
        {r"[^\S ]": ""}, regex=True
    )  # remove all whitespace except space

    print('Transform column "name" complete!')
    return new_series


def transform_all_column_dtype(df: pd.DataFrame):
    print("Transform all column dtype")
    return df.astype(SILVER_SCHEMA.get("crews"))


def clean():
    print(f"Cleaning bronze data: {df_name}")
    df = load_files_from_layer(layer="bronze", file_list=["crew.parquet"])["crew"]
    new_df = df.copy(True)

    print("Transforming columns")
    new_df["role"] = format_column_role(new_df["role"])
    new_df["name"] = format_column_name(new_df["name"])

    new_df = transform_all_column_dtype(new_df)

    new_df = process_duplicates(new_df, df_name)

    save_df(df=new_df, layer=destination_layer, df_name=clean_df_name)
    print("Cleaning complete!")
    return


def clean_enhanced():
    """
    Todo use parquet to enhance speed, and time it to compare the difference
    """
    return None
