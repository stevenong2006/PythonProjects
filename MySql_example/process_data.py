import pandas as pd
import numpy as np

df = pd.read_csv("Holdings_Realtime(11-18-2020).csv", index_col=False)

df['Time'] = pd.to_datetime(df['Time'].str[:-3], format= '%H:%M %p').dt.time

print(df.shape[1])

df.to_csv("Holdings_Realtime(11-18-2020)_edited.csv", index=False)

