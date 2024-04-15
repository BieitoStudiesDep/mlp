# import data
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# import utils
# from utils.printUtils import p
from utils.dfUtils import (  # dfGetColumnsWithNonNumericValues, dfGetColumnsWithNullValues,
    dfVerifiqueNullAndNotNumberValues,
    isDFThrow,
)


def FirstOheSequential(df: pd.DataFrame) -> pd.DataFrame:
    print("== OHE de manera secuencial ==")
    print("[Objetivo]")
    print("\t1.Cambiar los valores no numéricos por valores numéricos ")
    print("\t2.Cambiar los valores nulos por un valor representativo ")
    try:
        isDFThrow(df)
        dfVerifiqueNullAndNotNumberValues(df)
        # columnsWithNonNumericValues = dfGetColumnsWithNonNumericValues(df)
        # columnsWithNullValues = dfGetColumnsWithNullValues(df)

        print(" - Guardamos el indice de los valores nulos")
        print(
            "\tlos usaremos para validar si la imputación de los valores nulos es correcta"
        )

        ## para comprobar la efectividad de las operaciones que vamos a realizar
        ### obtenemos los índices de las filas con valores nulos
        null_rows_idx = df.isnull().any(axis=1)
        # p("split null_rows_idx", null_rows_idx)

        print(
            " - Aplicamos OHE a las columnas de valores no numéricos para trasformarlos en numéricos "
        )
        ## OHE
        ### Aplicamos también OneHotEncoder para las variables categóricas.
        cat_encoder = OneHotEncoder(sparse_output=False).set_output(
            transform="pandas"
        )  # forzamos que la salida sea DataFrame
        X_train_ocean_proximity_ohe = cat_encoder.fit_transform(df[["ocean_proximity"]])
        # p("X_train_ocean_proximity_ohe", X_train_ocean_proximity_ohe)

        print(
            " - Concatenamos las columnas donde aplicamos OHE con el resto del X_Train"
        )
        ### recuperar el resto de DataFrame
        ## Concatenamos los Dataframes
        ## entiendo que no es necesario ya que ya solo tenemos una salida
        X_train_rest = df.drop(columns="ocean_proximity")
        data_cat_ohe = pd.concat([X_train_rest, X_train_ocean_proximity_ohe], axis=1)
        # p("data_cat_ohe", data_cat_ohe)

        print(" - Estandarizamos valores : StandardScaler --> X_train_scaled_and_ohe ")
        ## Estandarización
        ## entiendo que como Aplique OHE todas las variables son de type int|float
        ## X_train_num = X_train.select_dtypes(include=[np.number]) 3 no es necesario
        scaler = StandardScaler().set_output(
            transform="pandas"
        )  # Para que el resultado sea un DataFrame
        X_train_scaled_and_ohe = scaler.fit_transform(data_cat_ohe)
        # p("X_train_scaled_and_ohe", X_train_scaled_and_ohe)

        print(" - Calculamos  k_value de manera manera estandarizada")
        # Calculamos k de manera manera estandarizada
        k_value = np.sqrt(df.shape[0]).astype(int)
        # p("k_value:", k_value)

        print(
            " - Imputamos valores :KNNImputer usando k_value y X_train_scaled_and_ohe"
        )
        ## Imputamos valores
        X_train_imputed_a = (
            KNNImputer(n_neighbors=k_value)
            .set_output(transform="pandas")
            .fit_transform(X_train_scaled_and_ohe)
        )
        # p("X_train_imputed_a", X_train_imputed_a)

        ## Verificamos
        print(" - verificamos")

        ## Verificamos la actualización de los valores nulos
        X_train_imputed_a.loc[
            null_rows_idx
        ].head()  # visualizamos las filas que tenían valores nulos

        return pd.DataFrame(X_train_imputed_a)

    except ValueError as ve:
        # Manejo de la excepción
        print("ValueError:", ve)
