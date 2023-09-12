import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/mtcars.csv")
print(data)
print(data.head(5))
print(data.info())
print(data.shape)
print(data.describe())
#univerate
print(data['mpg'].hist())
sns.countplot(x='am',data=data)
print(data['am'].value_counts())
print(data['mpg'].value_counts().plot(kind='bar'))
print(data['mpg'].plot.density())
print(sns.boxplot(x='mpg',data=data))
#biverate
print(sns.scatterplot(x=data['wt'],y=data['mpg']))
sns.countplot(x='am',hue='cyl',data=data)
#multiverate
print(sns.catplot(x='carb',hue='gear',col='vs',data=data,kind='count'))
print(sns.catplot(x='am',hue='carb',col='vs',data=data,kind='count'))



