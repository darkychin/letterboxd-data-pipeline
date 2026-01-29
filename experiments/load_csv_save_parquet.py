"""
Test script on what will happen to initial NA values after save into .parquet
"""

import pandas as pd

df_raw = pd.read_csv("data/external/actors.csv", dtype=str)

is_nas = df_raw["name"].isna() | df_raw["role"].isna()

print("raw nas:")
print(df_raw[is_nas])
print()

print("save to parquet")
path = "./data/test.parquet"
df_raw.to_parquet(path)
print()

print("load from parquet")
df_parquet = pd.read_parquet(path)
print()

print("parquet nas:")
is_pqrquet_nas = df_parquet["name"].isna() | df_parquet["role"].isna()
print(df_parquet[is_pqrquet_nas])
print()
print("Reuse `is_nas`")
print(df_parquet[is_nas])
print()
print("Single row check")
print(df_parquet.query("id == '1000047' & name == 'Ronan Hice'"))


# Conclusion for this script:
# `NaN` in df_raw will become `None` in df_parquet
