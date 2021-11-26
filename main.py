import numpy as np
import pandas as pd

dict = {'one': [10,np.nan,30], 'two': [np.nan, np.nan, 50], 'three': [10,10,10]}
df = pd.DataFrame(dict)
print(df)
print(df.dropna())
print(df.dropna(axis=1))
print(df)
print(df.dropna(thresh=2)) #2 не nan значения
print(df)
print(df.fillna(value='Something'))
print(df)
print(df['two'].fillna(value=df['two'].mean()))      #mean среднее значение
print(df)
print(df['one'].fillna(value=df['one'].mean()))
