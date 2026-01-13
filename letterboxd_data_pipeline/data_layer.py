from os import listdir
from letterboxd_data_pipeline.constants import DATA_LAYER_PATH


def validate_layer(layer: str):
    if layer not in DATA_LAYER_PATH:
        raise Exception("Invalid data source path!")
    return True


def get_file_path(layer: str) -> str | None:
    validate_layer(layer)

    return DATA_LAYER_PATH.get(layer)


def get_file_list(layer: str) -> tuple[list[str], str | None]:
    path = get_file_path(layer)

    return ([file for file in listdir(path)], path)
