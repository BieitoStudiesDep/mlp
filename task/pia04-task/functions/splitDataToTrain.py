# import data
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from utils.dfUtils import isDFThrow

# import utils


def SplitDataToTrain(df: pd.DataFrame) -> pd.DataFrame:
    try:
        isDFThrow(df)

        ###  split data to train
        ## split data to train
        X = df.drop(columns="median_house_value")
        y = df["median_house_value"]

        ### Muestreo estratificado (*Stratified sampling*)
        ### dividiendo el *dataset* en grupos llamados **estratos**,
        ### y asegurándose de tomar no solo un porcentaje de muestras del total,
        ### sino ese porcentaje de cada estrato.
        stratify = pd.cut(
            df["median_income"],
            bins=[
                0.0,
                1.5,
                3.0,
                4.5,
                6.0,
                np.inf,
            ],  # Secuencia de límites de los contenedores
            labels=[1, 2, 3, 4, 5],  # dividimos en 5 categorías
        )

        # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
        ## objetivo --> evitar el **sobre-ajuste** o ***over-fitting***
        ##  X_train, X_test, y_train, y_test = train_test_split(
        return train_test_split(
            X,  # features
            y,  # target
            stratify=stratify,  # estratificado
            test_size=0.2,  #  estoy usando el 20% de los datos # Controla la mezcla aplicada a los datos antes de aplicar la división.
            random_state=42,  ## fixed seed
        )
    except ValueError as ve:
        # Manejo de la excepción
        print("ValueError:", ve)
