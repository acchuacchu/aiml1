import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
df=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/iris.csv")
print(df)
print(df.head(10))
df.info()
df['Species'].count()
df['Species'].value_counts()
df.describe()
df.isna().sum
sns.heatmap(df.isna())
df.head(5)
df=df.drop(['Id'],axis=1)
df.info()
x=df.iloc[: , :-1]
print(x)
y=df.iloc[: , -1]
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8)
print("x test",x_test)
print("x train",x_train)
print("y test",y_test)
print("y train",y_train)

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion='entropy')
dtc.fit(x_train,y_train)
y_pred=dtc.predict(x_test)
print(y_pred)
print(y_train)

