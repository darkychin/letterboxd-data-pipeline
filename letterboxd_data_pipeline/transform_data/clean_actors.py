import pandas as pd
from letterboxd_data_pipeline.constants import DATA_LAYER_PATH
from letterboxd_data_pipeline.save_data import save_df
from letterboxd_data_pipeline.load_data import load_files_from_layer
from letterboxd_data_pipeline.transform_data.clean_common import general_clean
from letterboxd_data_pipeline.transform_data.schema import SILVER_SCHEMA

df_name = "actors"
clean_df_name = f"clean_{df_name}"
file_name = f"{df_name}.parquet"
source_path = DATA_LAYER_PATH.get("bronze")
destination_layer = "silver"
destination_path = DATA_LAYER_PATH.get(destination_layer)


def format_column_name(series: pd.Series[str]):
    # The following validation is ignored, because it does not impact Gold Layer aggregation
    # Read more here: docs/transformation-note.md
    # new_series = (series[~series.isna()]).str.contains(r"[\d\W_]")

    new_series = series.str.strip()

    print('Transform column "name" complete!')
    return new_series


def format_column_role(series: pd.Series[str | None]):
    # The following validation is ignored, because it does not impact Gold Layer aggregation
    # Read more here: docs/transformation-note.md
    # new_series = (series[~series.isna()]).str.contains(r"[\d\W_]")

    new_series = series.str.strip()

    print('Transform column "role" complete!')
    return new_series


def transform_all_column_dtype(df: pd.DataFrame):
    print("Transform all column dtype")
    return df.astype(SILVER_SCHEMA.get("actors"))


def drop_na_row(df: pd.DataFrame):
    target_na_rows = df["name"].isna() & df["role"].isna()
    row_count = target_na_rows.sum()

    if row_count:
        print(f"Dropping NA row count: {row_count}")
        return df[~target_na_rows]

    return df


def clean():
    df = load_files_from_layer(layer="bronze", file_list=[file_name])[df_name]
    new_df = df.copy(True)

    print()
    print(f"Cleaning bronze data: {df_name}")
    print("Transforming columns...")

    # Specific data cleaning
    new_df["name"] = format_column_name(new_df["name"])
    new_df["role"] = format_column_role(new_df["role"])
    new_df = transform_all_column_dtype(new_df)
    new_df = drop_na_row(new_df)
    print()

    # Generic data cleaning
    new_df = general_clean(new_df, df_name)

    print(f"Bronze data: {df_name} cleaning complete!")
    print()

    # Save clean data
    save_df(df=new_df, layer=destination_layer, df_name=clean_df_name)
    return


def clean_enhanced():
    """
    Todo use parquet to enhance speed, and time it to compare the difference
    """
    return None
