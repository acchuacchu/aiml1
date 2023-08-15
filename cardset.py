import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#read data
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/cardataset.csv ")[1:11]
print(data)
#staticial details of datset
stat=data.describe()
print(stat)
print(data['year'].min())
#get all cares with 8 cyclinder
print(data[data['cylinders']==8]['model'])
#number of cars manufactured in aeach year
print(data.groupby('year')['year'].value_counts())



