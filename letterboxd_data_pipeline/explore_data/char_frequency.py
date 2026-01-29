# Character Frequency Report
# - Naming credit to Google - Gemini AI

import pandas as pd
from collections import Counter


def gen_char_frequency_df(series: pd.Series[str]):
    """
    Docstring for gen_char_frequency_df

    :param series: Description
    :type series: pd.Series[str]

    Design reference:
    - https://stackoverflow.com/questions/31111032/transform-a-counter-object-into-a-pandas-dataframe/62031043#62031043
    - https://www.reddit.com/r/learnpython/comments/7kziie/comment/dridbq9/?context=3&utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    - Google - Gemini AI
    """

    all_chars = series.str.lower().str.cat()

    char_counts = Counter(all_chars)

    df = pd.DataFrame(char_counts.items(), columns=["character", "frequency"])

    return df.sort_values("frequency", ascending=False).reset_index(drop=True)
