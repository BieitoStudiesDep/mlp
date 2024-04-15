# import data
import pandas as pd

# ---------------------------------------------------------------------------------#


def DFCompare(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
) -> dict:
    res = {}

    # ❗Important to compare first reset index
    df1 = df1.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)

    res["df_size_eq"] = df1.shape == df2.shape
    res["df_data_type_eq"] = df1.dtypes.equals(df2.dtypes)
    res["df_columns_eq"] = df1.columns.equals(df2.columns)
    res["df_rows_eq"] = df1.index.equals(df2.index)
    res["df_value_00_eq"] = (df1.iloc[0, 0]) == (df2.iloc[0, 0])
    res["df_value_00_eq_round8"] = (df1.iloc[0, 0].round(8)) == (
        df2.iloc[0, 0].round(8)
    )
    res["df_values_eq"] = (df1 == df2).all().all()
    res["df_values_eq_round8"] = (df1.round(8) == df2.round(8)).all().all()
    return res
