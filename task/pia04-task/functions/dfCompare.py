# import data
# loading decimal library
from decimal import *

import pandas as pd


def DFCompare(df1: pd.DataFrame, df2: pd.DataFrame) -> str:
    DF_TYPE = "DataFrame"
    # Throw Exception
    if type(df1) != DF_TYPE:
        raise Exception("df1 is not a Dataframe")
    if type(df2) != DF_TYPE:
        raise Exception("df2 is not a Dataframe")
    if df1.size != df2.size:
        raise Exception("dif sinze")

    res = "Compare df1 vs df2"
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html

    res += "\n == compare types =="

    print("\n df1 types :\n", df1.dtypes)
    print("\n df2 types :\n", df2.dtypes)

    types_diff = df1.dtypes.difference(df2.dtypes)
    res += types_diff

    # column1_diff

    # row1_diff

    print("\n df1 (0,0) :\n", df1.iloc[1, 0])
    print("\n df2 (0,0) :\n", df2.iloc[1, 0])

    res += "\n == compare values =="
    first_value_diff_one_two = df1.iloc[1, 0].compare(df2.iloc[1, 0])
    res += "\ndf1.iloc[1, 0] VS df2.iloc[1, 0] --> " + first_value_diff_one_two
    first_value_diff_two_one = df2.iloc[1, 0].compare(df1.iloc[1, 0])
    res += "\ndf2.iloc[1, 0] VS df1.iloc[1, 0] --> " + first_value_diff_two_one

    # DataFrame Compare
    df1.compare(df2, align_axis=0)
    df1.compare(df2, keep_shape=True)
    df1.compare(df2, keep_shape=True, keep_equal=True)

    return res
