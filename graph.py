import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(data)
print(data.head(10))
plt.hist(data['Age'])
print(data['Age'].max())
print(data['Sex'].value_counts().plot(kind='bar'))
print(data[data['Pclass']==3]['Survived'].value_counts().plot(kind='bar'))
print(plt.scatter(x=data['Age'],y=data['Fare']))
print(sns.boxplot(data['Fare']))

