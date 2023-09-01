import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/tatanic 1.csv")
print(pd.DataFrame(data))
print(data['Age'].mean())
print(data.median())
print(data.mode())
print(data['Age'].mode())

speed=[12,45,77,85,7,89,46]
x=np.std(speed)
print(x)
print(len(speed))


