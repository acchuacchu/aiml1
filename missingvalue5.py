import pandas as pd
import seaborn  as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(data)
print(data.info())
print(data.isnull().sum())
print(data.isna().sum())
sns.heatmap(data.isna())
print(data.shape)
print(data.dropna(inplace=True))
print(data.shape)
df=data.drop(['Cabin'],axis=1)
print(df)
print(data.shape)
sns.heatmap(data.isna())
print(data.describe())

