import os
from pathlib import Path


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


def crawl_all_file_size(directory: str):
    """
    Crawl all file sizes in the directory

    :param directory: Description
    :type directory: str

    reference: https://stackoverflow.com/a/1392549/7939633
    """
    path = Path(directory)
    total = 0

    for file in path.glob("**/*"):
        if file.is_file():
            print(f"file: {file.name}")
            file_size = file.stat().st_size
            # ref
            # https://stackoverflow.com/a/12912296/7939633
            # https://stackoverflow.com/a/52684562/7939633
            print(f"size: {file_size / (1 << 20)} MB")
            total += file_size

    print(f"total size: {total / (1 << 30)} GB")
