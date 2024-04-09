# Modificación del ejemplo de KNNImputer haciendo OHE antes de la estándarización.

## OHE -OneHotEncoder

```python
# import data
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

## assigned data
housing = pd.read_csv("./data/housing.csv")

## split data to train
X = housing.drop(columns="median_house_value")
y = housing["median_house_value"]
print("\ndata X value:",X)
print("\ndata y value:",y)

### Muestreo estratificado (*Stratified sampling*)
### dividiendo el *dataset* en grupos llamados **estratos**,
### y asegurándose de tomar no solo un porcentaje de muestras del total,
### sino ese porcentaje de cada estrato.
stratify = pd.cut(
    housing["median_income"],
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
print("\nstratify data:",stratify)

# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
## objetivo --> evitar el **sobre-ajuste** o ***over-fitting***
X_train, X_test, y_train, y_test = train_test_split(
    X,  # features
    y,  # target
    stratify=stratify,  # estratificado
    test_size=0.2,  #  estoy usando el 20% de los datos # Controla la mezcla aplicada a los datos antes de aplicar la división.
    random_state=42,  ## fixed seed
)
X_train
print("\nsplit X_train:","type:",X_train.d,",value",X_train)
print("\nsplit X_train:","type",",value",X_test)
print("\nsplit X_train:","type",",value",y_train)
print("\nsplit X_train:","type",",value",y_test)

## para comprobar la effectividad de las operaciones que vamos a realizar
### obtenemos los índices de las filas con valores nulos
null_rows_idx = X_train.isnull().any(axis=1)
null_rows_idx

# Calculamos k de manera manera estandarizada
k_value = np.sqrt(X_train.shape[0]).astype(int)
k_value

## OHE
### Aplicamos también OneHotEncoder para las variables categóricas.
cat_encoder = OneHotEncoder(sparse_output=False).set_output(
    transform="pandas"
)  # forzamos que la salida sea DataFrame
X_train_ocean_proximity_ohe = cat_encoder.fit_transform(X_train[["ocean_proximity"]])
X_train_ocean_proximity_ohe

### recuperar el resto de DataFrame
## Concatenamos los Dataframes
## entiendo que no es necesario ya que ya solo tenemos una salida
X_train_rest = X_train.drop(columns="ocean_proximity")
housing_cat_ohe = pd.concat([X_train_rest, X_train_ocean_proximity_ohe], axis=1)
housing_cat_ohe

## Estandarización
## entiendo que como Aplique OHE todas las variables son de type int|float
## X_train_num = X_train.select_dtypes(include=[np.number]) 3 no es necesario
scaler = StandardScaler().set_output(
    transform="pandas"
)  # Para que el resultado sea un DataFrame
X_train_scaled_and_ohe = scaler.fit_transform(housing_cat_ohe)
X_train_scaled_and_ohe

## Imputamos valores
X_train_imputed_a = (
    KNNImputer(n_neighbors=k_value)
    .set_output(transform="pandas")
    .fit_transform(X_train_scaled_and_ohe)
)
X_train_imputed_a

## Verificamos que no hay valores nulos
print(X_train_imputed_a.isna().any().any())
X_train_imputed_a

## Verificamos la actualización de los valores nulos
X_train_imputed_a.loc[
    null_rows_idx
].head()  # visualizamos las filas que tenían valores nulos