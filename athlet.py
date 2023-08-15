import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/athele events.csv")
data1=pd.DataFrame(data)
print(data1)

plt.hist(data['Age'])
print(data['Age'].max())
plt.show()


plt.scatter(data['Height'],data['Weight'])
plt.show()


print(data['Height'].value_counts())
plt.bar(data['Height'],data['Weight'])

plt.show()

