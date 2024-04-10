# import data
import numpy as np
import pandas as pd
from sklearn.compose import (
    ColumnTransformer,
    make_column_selector,
    make_column_transformer,
)
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline, make_pipeline
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


# try 1
# ---------------------------------------------------------------------------------#


def preprocess_and_impute(df):
    k_value = int(np.sqrt(df.shape[0]))
    # Identificar las columnas categóricas y numéricas
    categorical_columns = df.select_dtypes(include=["object"]).columns
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns

    # Crear un ColumnTransformer que aplique OneHotEncoder a las columnas categóricas
    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(), categorical_columns)],
        remainder="passthrough",  # Dejar pasar las columnas numéricas
    )

    # Crear un Pipeline que incluya el preprocesamiento y luego aplique StandardScaler
    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "scaler",
                StandardScaler(with_mean=False),
            ),  # with_mean=False para manejar datos dispersos
        ]
    )

    # Aplicar el Pipeline al DataFrame
    df_transformed = pipeline.fit_transform(df)

    # Aplicar KNNImputer al resultado del Pipeline
    imputer = KNNImputer(n_neighbors=k_value)
    df_imputed = imputer.fit_transform(df_transformed)

    # Convertir el resultado imputado de nuevo a un DataFrame
    # Necesitamos obtener los nombres de las nuevas columnas después de OHE y escalar
    ohe_columns = (
        pipeline.named_steps["preprocessor"]
        .named_transformers_["cat"]
        .get_feature_names_out()
    )
    all_columns = np.concatenate([ohe_columns, numerical_columns])

    imputed_df = pd.DataFrame(df_imputed, columns=all_columns)

    return move_columns_to_end_by_len(imputed_df, len(ohe_columns))


# try 2
# ---------------------------------------------------------------------------------#


def preprocess_and_impute2(df):
    ## Definir el número k para KNNImputer
    k_value = int(np.sqrt(df.shape[0]))
    all_numerical_features = df.select_dtypes(include=["int64", "float64"]).columns
    # print(all_numerical_features)
    all_categorical_features = df.select_dtypes(include=[object]).columns
    # print(all_categorical_features)

    numerical_features = [value for value in all_numerical_features]
    categorical_features = [value for value in all_categorical_features]

    print(numerical_features)
    print(categorical_features)
    transformer = make_column_transformer(
        (
            OneHotEncoder(handle_unknown="ignore", sparse_output=False),
            make_column_selector(dtype_include="object"),
        ),  # Aplica OneHotEncoder a las columnas categóricas
        (
            StandardScaler(),
            make_column_selector(dtype_exclude="object"),
        ),
        # Aplica StandardScaler a las columnas numéricas
        remainder="passthrough",  # Conserva las columnas que no se transforman
        sparse_threshold=0.1,
        n_jobs=3,
        # remainder="drop",  # Conserva las columnas que no se transforman
    )
    # Crear un pipeline que incluya el ColumnTransformer y el KNNImputer
    pipeline = make_pipeline(transformer, KNNImputer(n_neighbors=k_value))

    # Aplicar el pipeline a los datos de entrenamiento
    X_train_imputed_b = pipeline.fit_transform(df)
    X_train_imputed_b
    # Convertir el resultado a DataFrame
    imputed_df = pd.DataFrame(
        X_train_imputed_b,
        columns=transformer.get_feature_names_out(),
        index=df.index,
    )
    # Obtener los nombres de las columnas de OneHotEncoder
    ohe_columns = transformer.transformers_[0][1].get_feature_names_out()
    return move_columns_to_end_by_len(imputed_df, len(ohe_columns))


# try 3
# ---------------------------------------------------------------------------------#


def preprocess_and_impute3(df):
    ## Definir el número k para KNNImputer
    k_value = int(np.sqrt(df.shape[0]))
    # Identificar las columnas categóricas y numéricas
    categorical_columns = df.select_dtypes(include=["object"]).columns
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns

    # Crear un ColumnTransformer con make_column_transformer
    preprocessor = make_column_transformer(
        (OneHotEncoder(), categorical_columns),
        remainder="passthrough",  # Dejar pasar las columnas numéricas
    )

    # Crear un Pipeline con make_pipeline
    pipeline = make_pipeline(
        preprocessor,
        StandardScaler(with_mean=False),  # with_mean=False para manejar datos dispersos
    )

    # Aplicar el Pipeline al DataFrame
    df_transformed = pipeline.fit_transform(df)

    # Aplicar KNNImputer al resultado del Pipeline
    imputer = KNNImputer(n_neighbors=k_value)
    df_imputed = imputer.fit_transform(df_transformed)

    # Obtener los nombres de las nuevas columnas después de OHE y escalar
    ohe_columns = preprocessor.named_transformers_[
        "onehotencoder"
    ].get_feature_names_out()
    all_columns = np.concatenate([ohe_columns, numerical_columns])

    # Convertir el resultado imputado de nuevo a un DataFrame
    imputed_df = pd.DataFrame(df_imputed, columns=all_columns)

    print(type(ohe_columns))
    print(ohe_columns)
    return move_columns_to_end_by_len(imputed_df, len(ohe_columns))
    # mc2 = move_columns_to_end_by_name(imputed_df, ohe_columns.tolist())


# Public Function
# ---------------------------------------------------------------------------------#


def FirstOhePipe(df: pd.DataFrame) -> pd.DataFrame:
    try:
        isDFThrow(df)
        imputed_df, mc1, mc2 = preprocess_and_impute3(df)
        print("\nimputed_df\n", imputed_df)
        print("--------------------------------------")
        print("\mc1\n", mc1)
        print("--------------------------------------")
        print("\mc2\n", mc2)
        return pd.DataFrame()
    except ValueError as ve:
        # Manejo de la excepción
        print("ValueError:", ve)
