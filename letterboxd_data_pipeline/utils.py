import os

def make_data_path(path):
    """
    Make path
    make_data_path("./data/external")
    """
    if not os.path.exists(path):
        print(f"Creating path: {path}")
        os.makedirs(path)


def compare_file_size():
    """
    Testing on csv size vs parquet

    movies.csv vs movies parquet, parquet reduce by size for around 32%
    """
    csv_size = os.stat("./data/external/movies.csv").st_size
    parquet_size = os.stat("./data/bronze/movies").st_size
    print("csv: ", csv_size)
    print("parquet: ", parquet_size)
    print("%reduce: ", (csv_size - parquet_size) / csv_size * 100)