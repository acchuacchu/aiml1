import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(data)
sns.catplot(x='Embarked',hue='Survived',col='Sex',data=data,kind='count')
sns.catplot(x='Pclass',hue='Sex',col='Survived',data=data,kind='count')
