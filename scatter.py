import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv ")
print(data)
plt.scatter(data['Age'],data['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title("scatter plot graph")
plt.show()







