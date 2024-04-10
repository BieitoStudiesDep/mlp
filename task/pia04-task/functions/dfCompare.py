# import data
# loading decimal library
from decimal import *
from typing import List

import pandas as pd

# ---------------------------------------------------------------------------------#


def media_precision_decimales_by_Df(df1, df2):
    precision_decimales = []
    # Iterar sobre las filas y comparar los valores de decimales
    for index, (fila1, fila2) in enumerate(zip(df1.iterrows(), df2.iterrows())):
        for col in df1.select_dtypes(include=["float64"]).columns:
            # Comprobar si los valores de los decimales son iguales
            if fila1[1][col] == fila2[1][col]:
                # Calcular la precisión de los decimales
                precision_decimales.append(len(str(fila1[1][col]).split(".")[1]))

    # Calcular la media de la precisión de los decimales
    if precision_decimales:
        media = sum(precision_decimales) / len(precision_decimales)
    else:
        media = 0

    return media


def media_precision_decimales_by_index(df1, df2, indices):
    precision_decimales = []

    # Iterar sobre los índices proporcionados
    for idx in indices:
        # Obtener las filas correspondientes en los DataFrames
        fila1 = df1.loc[idx]
        fila2 = df2.loc[idx]

        # Iterar sobre las columnas numéricas
        for col in df1.select_dtypes(include=["float64"]).columns:
            # Comprobar si los valores de los decimales son iguales
            if fila1[col] == fila2[col]:
                # Calcular la precisión de los decimales
                precision_decimales.append(len(str(fila1[col]).split(".")[1]))

    # Calcular la media de la precisión de los decimales
    if precision_decimales:
        media = sum(precision_decimales) / len(precision_decimales)
    else:
        media = 0

    return media


# function main
# ---------------------------------------------------------------------------------#


def DFCompare(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    onehotencoder_column_indexs: List[int] = None,
    index_null_values: List[int] = None,
) -> dict:
    result = {
        "df-size-eq": df1.shape == df2.shape,
        "df-dataType-eq": df1.dtypes.equals(df2.dtypes),
        "df-columns-eq": df1.columns.equals(df2.columns),
        "df-rows-eq": df1.index.equals(df2.index),
        "df-values-eq": (df1 == df2).all().all(),
    }

    if onehotencoder_column_indexs is not None:
        result["df-decimals-onehotencoder-values-media"] = (
            media_precision_decimales_by_index(
                df1.iloc[:, onehotencoder_column_indexs],
                df2.iloc[:, onehotencoder_column_indexs],
            )
        )

    if index_null_values is not None:
        result["df-decimals-index-null-values-media"] = (
            media_precision_decimales_by_index(df1, df2, index_null_values)
        )

    return result
