import pandas as pd
import numpy as np

std=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/stu_mar.csv")
print(std)
mrk=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/stu_id.csv")
print(mrk)
mrg=pd.merge(std,mrk)
print(mrg)



