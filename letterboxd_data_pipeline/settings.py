from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path

def __load_env():
    """
    Load the .env content to os
    """
    current_path = dirname(__file__)
    # print(current_path)

    # pyproject.toml treat letterboxd_data_pipeline as a package, so we only need to go up one level 
    parent_path = str(Path(current_path).parents[0])
    print(parent_path)

    dotenv_path = join(parent_path, ".env")
    print("Load .env from ", dotenv_path)

    load_dotenv(dotenv_path)
    print("Load completed")


def init():
    __load_env()


if __name__ == "__main__":
    init()


# SECRET_KEY = os.environ.get("SECRET_KEY")
# DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

# References
# - Go up in path: https://stackoverflow.com/a/51524232/7939633
# - no side effect during import: https://chrismorgan.info/blog/say-no-to-import-side-effects-in-python/
# - init() design: https://stackoverflow.com/a/6523855/7939633
