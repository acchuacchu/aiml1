import pandas as pd
import seaborn  as sns
import numpy as np
df=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(df)
df.duplicated(subset=None,keep="first").sum()
print(df)
df.drop_duplicates(subset=None,keep="first",inplace=True)
df.shape

