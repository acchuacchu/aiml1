import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(data)
df=data.isna().sum()
print(data['Age'].fillna(df,inplace=True))
sns.boxplot(data['Age'])
Q1=data['Age'].quantile(0.25)
print(Q1)
Q3=data['Age'].quantile(0.75)
print(Q3)
IQR=Q3-Q1
print(IQR)
lw=Q1-(1.5*IQR)
print("lower whisker",lw)
uw=Q3+(1.5*IQR)
print("upper whiskre",uw)
data['Age']=np.where(data['Age']>uw,uw,np.where(data['Age']<lw,lw,data['Age']))
print(data['Age'])
sns.boxplot(data['Age'])                                                                       
ind=(data['Age']>uw)|(data['Age']<lw)
print(ind)
index=data[ind].index
print(index)
data.drop(index,inplace=True)
sns.boxplot(data['Age'])

