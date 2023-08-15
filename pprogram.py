import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tdataset.csv ")
print(data)
print(data['Survived'].value_counts().plot(kind='bar'))
print(data['Survived'].value_counts())
print(data[data['Sex']=='female']['Survived'].value_counts())
print(data[data['Pclass']==1]['Survived'].value_counts().plot(kind='bar'))
plt.scatter(x=data['Age'],y=data['Fare'])
plt.hist(data['Age'])
print(data['Survived'].value_counts())
print(data[data['Sex']=='female']['Survived'].value_counts().plot(kind='bar'))


