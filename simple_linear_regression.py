import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/esl.csv")
print(data)
print(data.isna().sum())
x=data['YearsExperience'].values.reshape(-1,1)
print(x)
y=data['Salary'].values.reshape(-1,1)
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
print(x_train)
print(x_test)   
print(y_train)
print(y_test)

from sklearn.linear_model import LinearRegression

m=LinearRegression()
print(m.fit(x_train,y_train))
pre=m.predict(x_test)
print(pre)








