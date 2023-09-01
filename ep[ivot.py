import pandas as pd
import numpy as np
a=pd.DataFrame({'first name':['racchu','acchu','paru','nagu'],
                'type':['fulltime employe','parttime employe','intern','fulltime employe'],
                'salary':[17009,25422,20000,57558],
                'yoe':[2,5,7,3],'department':['administratin','technical','management','adminstration']})
print(a)
table=a.pivot_table(index=['type','department'],values='salary',aggfunc='mean')
print(table)
table1=a.pivot_table(index='type',values='salary',aggfunc=['mean','sum','count'])
print(table1)












