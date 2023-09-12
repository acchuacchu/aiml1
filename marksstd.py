import pandas as pd
import numpy as np

std=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/stu_mar.csv")
print(std)
mrk=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/stu_id.csv")
print(mrk)
total=[450,687,654,398,545,765,335,100,32,197,176,973,527,244,425,165,154,198,152,21,165,862,175,217,622,762,762,657,872]
m=mrk.assign(total_marks=total)
print(m)
m1=m.assign(percentage=list(map(lambda x : x*100/2900,m['total_marks'])))
print(m1)
new=m.insert(1,'mrk_indexing',total)
print(new)
new1=new.assign(a=None,b=0)
print(new1)

