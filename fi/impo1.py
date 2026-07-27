import pandas as pd
from pandas import DataFrame as DF, Series as SR

import os, sys

data = {
    "Name": ["Yash", "John", "Alice"],
    "Age": [23, 25, 22],
    "City": ["Hyderabad", "Delhi", "Mumbai"],
}


df = pd.DataFrame(data)


print(df)
