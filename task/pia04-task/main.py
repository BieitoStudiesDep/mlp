# import lib
import pandas as pd

# import functions
from functions.dfCompare import DFCompare
from functions.firstOhePipe import FirstOhePipe
from functions.firstOheSequential import FirstOheSequential
from functions.splitDataToTrain import SplitDataToTrain

df = pd.read_csv("./data/housing.csv")


X_train, X_test, y_train, y_test = SplitDataToTrain(df)

ohe_sequential = FirstOheSequential(X_train.copy())
ohe_pipe = FirstOhePipe(X_train.copy())

compare = DFCompare(ohe_sequential, ohe_pipe)
