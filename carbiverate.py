import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/cardataset.csv")[:5]
print(data)
sns.scatterplot(x=data['year'],y=data['cylinders'])
plt.scatter(data['year'],data['cylinders'])
sns.countplot(x='model',hue='brand',data=data)
sns.countplot(x='cylinders',hue='brand',data=data)
sns.countplot(x='cylinders',hue='model',data=data)
sns.countplot(x='color',hue='brand',data=data)
sns.countplot(x='color',hue='cylinders',data=data)




