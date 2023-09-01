import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(data)
matrix=data.corr()
print(matrix)
sns.heatmap(matrix,cmap='YlGnBu')
