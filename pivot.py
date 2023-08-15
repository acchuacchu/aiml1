import pandas as pd
import numpy as np
data=pd.DataFrame({'product':['mango','apple','orange','watermellon'],'catagories':['f','r','m','a'],
       'quantity':[10,35,76,84],'amount':[124,56,86,43]})

table=data.pivot_table(index='product',values='amount',aggfunc='sum')
print(table)

 
