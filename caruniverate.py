import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/cardataset.csv")
print(data)
print(data.head(5))
print(data.info())
print(data.shape)
print(data.describe())
print(data['year'].hist())
sns.countplot(x='cylinders',data=data)
data['cylinders'].value_counts()
sns.countplot(x='model',data=data)
data['year'].value_counts().plot(kind='bar')
data['year'].plot.density()
sns.boxplot(x='year',data=data)
sns.countplot(x='model',data=data)
