# import data
import pandas as pd

# import utils
from utils.dfUtils import isDFThrow


def FirstOhePipe(df: pd.DataFrame) -> pd.DataFrame:
    try:
        isDFThrow(df)

        return pd.DataFrame()
    except ValueError as ve:
        # Manejo de la excepción
        print("ValueError:", ve)
