import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv ")
print(data)
print(plt.hist(data['Age']))
print(data['Age'].max())
plt.show()



