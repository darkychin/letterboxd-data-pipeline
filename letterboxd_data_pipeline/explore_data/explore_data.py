import pandas as pd
from letterboxd_data_pipeline.constants import POSSIBLE_NA_LIST


def shallow_explore(df):
    print("Explore top 5 data")
    for data in df:
        print(df[data].head(5))


def deep_explore(df: pd.DataFrame, name):
    target = df[name]
    print(f"Exploring name: {name}")
    print("=======================================")
    print(target.head(5))
    print(target.tail(5))
    print(target.info())
    print(target.describe())
    print()


# def experimental_explore(raw_df: pd.DataFrame):
#     # non_number_minute = df[math.isnan(int(df["minute"]))]

#     df = raw_df.copy()
#     na_minute = raw_df.copy()["minute"].isna()
#     clean_minute = raw_df.copy().dropna()
#     # print(clean_minute.head())
#     print(clean_minute.describe())
#     print(clean_minute.groupby("minute").count())
#     # print(non_number_minute.groupby("minute").count())


def deep_explore_all(df):
    pd.set_option("display.max.columns", None)
    for data in df:
        deep_explore(df=df, name=data)


def is_possible_na(series: pd.Series[str]):
    return series.str.lower().isin(POSSIBLE_NA_LIST)
