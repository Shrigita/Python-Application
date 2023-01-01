import pandas as pd 
import numpy as np 

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
print(s[0])

data = np.array(['a','b','c','d'])
s = pd.Series(data,index = [100,101,102,103])
print(s)

data ={'a' : 0.1 ,'b' : 1.1 ,'c':2.1}
s = pd.Series(data)
print(s)

s = pd.Series([1,2,3,4,5],index =['a','b','c','d','e'])
print(s)
print(s['a'])