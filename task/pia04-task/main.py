# import lib
import pandas as pd

# import functions
from functions.dfCompare import DFCompare
from functions.firstOhePipe import FirstOhePipe
from functions.firstOheSequential import FirstOheSequential
from functions.splitDataToTrain import SplitDataToTrain

df = pd.read_csv("task/pia04-task/data/housing.csv")

print(" == Step1 Split Data to Train ==")
X_train, X_test, y_train, y_test = SplitDataToTrain(df)
print(" == Step2 OHE sequential ==")
ohe_sequential = FirstOheSequential(X_train.copy())
print(" == Step1 OHE pipe ==")
ohe_pipe = FirstOhePipe(X_train.copy())
print(" == Step1 Compare OHE sequential vs OHE pipe ==")
compare = DFCompare(ohe_sequential, ohe_pipe)
