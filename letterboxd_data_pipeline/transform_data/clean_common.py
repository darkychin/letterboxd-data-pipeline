import pandas as pd
import re
from letterboxd_data_pipeline.save_data import save_df
from letterboxd_data_pipeline.constants import POSSIBLE_NA_LIST


def process_duplicates(df: pd.DataFrame, df_name: str):
    LAYER = "silver"
    prefix = "duplicated_"

    duplicates_df_name = f"{prefix}{df_name}"
    duplicates_df = df[df.duplicated]
    size = duplicates_df.size

    if size:
        print(f"Duplicated rows found: {size}")
        save_df(df=duplicates_df, layer=LAYER, df_name=duplicates_df_name)

    return df.drop_duplicates()


def format_column_name(name: str):
    new_name = name.lower()
    # reference  https://stackoverflow.com/questions/11475885/python-replace-regex
    new_name = re.sub("[ -?!.&]", "_", name)

    if name != new_name:
        print(f"Replace column name: {name} -> {new_name}")

    return new_name


def format_df_columns(df: pd.DataFrame):
    # reference https://stackoverflow.com/questions/50177359/rename-variously-formatted-column-headers-in-pandas
    return df.rename(columns=format_column_name)


def filter_possible_na(df: pd.DataFrame):
    new_df = df.copy(True)

    for column in new_df.columns:
        # We assume that there should be no complex object in the data (todo: need to verify)
        if new_df[column].dtype == "object":
            print(f"Scanning column: {column}")
            possible_na_rows = new_df[column].str.lower().isin(POSSIBLE_NA_LIST)
            row_count = possible_na_rows.sum()
            print(f"number of possible na row found: {row_count}")
            print("possible na row:")
            print(possible_na_rows)
            # new_df[column].apply(lambda x: None if x in na_list else x)
            # todo stop here
    return new_df


def general_clean(df: pd.DataFrame, df_name: str):
    new_df = process_duplicates(df, df_name)
    new_df = format_df_columns(new_df)
    return new_df
