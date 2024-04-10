import pandas as pd


def isSeries(series: pd.Series) -> bool:
    """Check if the input is a Pandas Series."""
    return isinstance(series, pd.Series)


def isSeriesThrow(series: pd.Series):
    """Check if the input is a Pandas Series, if not, raise ValueError."""
    if not isinstance(series, pd.Series):
        raise ValueError("series is not a Series")


def seriesGetFirstValue(series: pd.Series):
    """Get the first value of the Series."""
    return series.iloc[0]


def seriesCompare(series1: pd.Series, series2: pd.Series) -> pd.Series:
    """Compare two Series and return the comparison result."""
    return series1.compare(series2)


def seriesEqu(series1: pd.Series, series2: pd.Series) -> dict:
    """
    Compare two Series element-wise and return a dictionary containing:
    1. A Series of boolean values indicating equality.
    2. A boolean value indicating if all elements are equal.
    3. A boolean value indicating if any element is equal.
    """
    series_bool = series1.eq(series2)
    all_values_equal = series_bool.all()
    any_value_equal = series_bool.any()
    return {
        "series_bool": series_bool,
        "all_values_equal": all_values_equal,
        "any_value_equal": any_value_equal,
    }
