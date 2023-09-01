
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#read data
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/auto-mpg.csv")
print(data)
print(data.head(10))
plt.hist(x=data['mpg'])
plt.scatter(x='weight',y='mpg',data=data)
data['origin'].value_counts().plot(kind='bar')
sns.boxplot(data['mpg'])
print("min",data['mpg'].min())

