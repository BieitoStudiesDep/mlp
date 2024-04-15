# import data
import numpy as np
import pandas as pd
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.impute import KNNImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# import utils
from utils.dfUtils import isDFThrow

# Move DF columns
# ---------------------------------------------------------------------------------#


def move_columns_to_end_by_len(df: pd.DataFrame, num_columns: int) -> pd.DataFrame:
    # Revisar si el número de columnas a mover es válido
    if num_columns >= len(df.columns):
        print(
            "El número de columnas a mover excede el número total de columnas en el DataFrame."
        )
        return df

    # Reordenar las columnas
    cols = list(df.columns)
    cols = cols[num_columns:] + cols[:num_columns]
    df = df[cols]

    return df


def move_columns_to_end_by_name(
    df: pd.DataFrame, columns_to_move: list
) -> pd.DataFrame:
    # Revisar si los nombres de columnas son válidos
    invalid_columns = [col for col in columns_to_move if col not in df.columns]
    if invalid_columns:
        print(f"Las siguientes columnas no existen en el DataFrame: {invalid_columns}")
        return df

    # Reordenar las columnas
    cols = [col for col in df.columns if col not in columns_to_move] + columns_to_move
    df = df[cols]
    return df


def FirstOhePipe(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # comprobaciones
        isDFThrow(df)
        # definimos variables
        k_value = int(np.sqrt(df.shape[0]))
        # Identificar las columnas categóricas y numéricas
        categorical_columns = df.select_dtypes(include=["object"]).columns
        numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns

        # Crear un Pipeline
        ##  1. ejecute OHE - OneHotEncoder
        ###  - dtype_include="object" --> aplicamos solamente a datos no numericos
        ###  -  remainder="passthrough" --> tras aplicar los cambios necesitamos recuperar el resto de columnas
        ##  2. estandarice - StandardScaler
        ##  3. impute los datos nulos o faltantes - KNNImputer
        pipeline = make_pipeline(
            make_column_transformer(
                (OneHotEncoder(), make_column_selector(dtype_include="object")),
                remainder="passthrough",
            ),
            StandardScaler(),
            KNNImputer(n_neighbors=k_value),
        )
        # Aplicamos las trasformaciones y las imputaciones al DataFrame
        array_transformed = pipeline.fit_transform(df)
        # Convertir el resultado imputado de nuevo a un DataFrame
        ## Necesitamos obtener los nombres de las nuevas columnas después de OHE y el resto
        ohe_columns = (
            pipeline.named_steps["columntransformer"]
            .named_transformers_["onehotencoder"]
            .get_feature_names_out(input_features=categorical_columns)
        )
        all_columns = np.concatenate([ohe_columns, numerical_columns])
        # Generamos un nuevo DF
        df_transformed = pd.DataFrame(array_transformed, columns=all_columns)
        # nota las columnas ohe se colocan al principio del df, las ponemos al final
        # para que coincidan con eñ resultado secuencial
        return move_columns_to_end_by_len(df_transformed, len(ohe_columns))

    except ValueError as ve:
        # Manejo de la excepción
        print("ValueError:", ve)
