import pandas as pd


def isDF(df: pd.DataFrame) -> bool:
    """Check if the input is a Pandas DataFrame."""
    return isinstance(df, pd.DataFrame)


def isDFThrow(df: pd.DataFrame):
    """Check if the input is a Pandas DataFrame, if not, raise ValueError."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df is not a DataFrame")


def dfGetFirstRowAsSeries(df: pd.DataFrame) -> pd.Series:
    """Get the first row of the DataFrame as a Series."""
    return df.iloc[0]


def dfGetFirstColAsSeries(df: pd.DataFrame) -> pd.Series:
    """Get the first column of the DataFrame as a Series."""
    return df.iloc[:, 0]


def dfGetFirstColAsDF(df: pd.DataFrame) -> pd.DataFrame:
    """Get the first column of the DataFrame as a DataFrame."""
    return df.iloc[:, :1]


def dfGetFirstPosition(df: pd.DataFrame):
    """Get the value at the first row and first column of the DataFrame."""
    return df.iloc[0, 0]


def dfCompare(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Compare two DataFrames and return the comparison result."""
    return df1.compare(df2, align_axis=0)
    # res = ""
    # # DataFrame Compare
    # df1.compare(df2, align_axis=0)
    # df1.compare(df2, keep_shape=True)
    # df1.compare(df2, keep_shape=True, keep_equal=True)
    # return res


def dfEqu(df1: pd.DataFrame, df2: pd.DataFrame) -> dict:
    """
    Compare two DataFrames element-wise and return a dictionary containing:
    1. A DataFrame of boolean values indicating equality.
    2. A boolean value indicating if all elements are equal.
    3. A boolean value indicating if any element is equal.
    """
    df_bool = df1.eq(df2)
    all_parm_true = df_bool.all().all()
    any_parm_true = df_bool.any().any()
    return {
        "df_bool": df_bool,
        "all_parm_true": all_parm_true,
        "any_parm_true": any_parm_true,
    }
