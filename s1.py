import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#read data
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/HRDataset_v14.csv ")
print(data)

print(data[data['Sex']=='M']['Department']=='IT/IS')

print(data[data['Sex']=='F']['Department']=='Production')
a=data.groupby('Department')['Salary'].sum()
print(a)
print(data[data['Sex']=='M']['Salary']>53250)

