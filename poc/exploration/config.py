# Import cross module solution for jupyter notebook
# - https://stackoverflow.com/a/35273613/7939633
# - https://stackoverflow.com/a/44486700/7939633
import os
import sys

module_path = os.path.abspath(os.path.join(".."))

if module_path not in sys.path:
    sys.path.append(module_path)
