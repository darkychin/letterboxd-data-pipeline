# Setup working directory on run time for main.py to work correctly with project absolute import:
# - https://stackoverflow.com/a/71057808/7939633
# - https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c/
# - https://stackoverflow.com/a/35273613/7939633
# - https://stackoverflow.com/a/44486700/7939633
import sys, os

module_path = os.path.abspath(os.path.join(".."))

if module_path not in sys.path:
    # Set python system path to "/poc/"
    sys.path.append(module_path)

import letterboxd_data_pipeline.settings as settings

# Setup environment and configs for kaggle
settings.init()

import letterboxd_data_pipeline.extract_data.download_data as download_data
from letterboxd_data_pipeline.load_data import load_files_from_layer
from letterboxd_data_pipeline.explore_data import shallow_explore
from letterboxd_data_pipeline.save_data import save_all_data


def extract():
    # note importing download data already trigger Kaggle env credential verification, due to their API designs....
    return download_data.start()


def load_from_external(target_file_list: list[str]):
    return load_files_from_layer(layer="external", file_list=target_file_list)


def explore(df):
    # for detail exploration, go to "../exploration"
    shallow_explore(df)


def save_checkpoint(layer: str, df):
    save_all_data(df, layer)


def load_checkpoint(layer):
    return load_files_from_layer(layer=layer)


target_file_list = extract()

letterboxd_dict = load_from_external(target_file_list)

explore(letterboxd_dict["countries"])

save_checkpoint("bronze", letterboxd_dict)

letterboxd_dict = load_checkpoint("bronze")
