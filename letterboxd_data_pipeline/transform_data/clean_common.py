import pandas as pd
from letterboxd_data_pipeline.save_data import save_df

LAYER = "silver"


def process_duplicates(df: pd.DataFrame, df_name: str):
    prefix = "duplicated_"
    duplicates_df_name = f"{prefix}{df_name}"
    duplicates_df = df[df.duplicated]
    size = duplicates_df.size

    if size:
        print(f"Duplicated rows found: {size}")
        save_df(df=duplicates_df, layer=LAYER, df_name=duplicates_df_name)

    return df.drop_duplicates()
