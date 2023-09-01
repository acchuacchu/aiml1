
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dummy_age=[12,43,12,45,12,45]
dummy_sex=['female','male','male','male','male','female']

df=pd.DataFrame({'age':dummy_age,'sex':dummy_sex})
print(df)
print(df['age'].hist())

sns.set(style='darkgrid')
a=sns.countplot(x='sex',data=df)
