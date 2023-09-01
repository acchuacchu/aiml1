import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(data)
print(data.head(5))
print(data.info())
print(data.shape)
print(data.describe())
print(data['Age'].hist())
sns.countplot(x='Pclass',data=data)
data['Pclass'].value_counts()
sns.countplot(x='Sex',data=data)
data['Age'].value_counts().plot(kind='bar')
data['Age'].plot.density()
sns.boxplot(x='Age',data=data)
sns.countplot(x='Sex',data=data)

