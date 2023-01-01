import pandas as pd 

#DataFrame with list
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data =[['PPA',4,18000],['LB',3,18200],['Python',3,18500]]
df= pd.DataFrame(data,columns =['Name','Duration','Fee'])
print(df)

data = {'Name ':['PPA','LB','Python'],'Duration': [4,3,3],'Fee' :[18000,18200,18500]}
df = pd.DataFrame(data)
print(df)

data =[{'Name': 'PPA','Duration ': 3,'Fee':18000},{'Name': 'PPA','Duration ': 3,'Fee':18000},{'Name': 'Python','Duration ': 3,'Fee':18050}]
df =pd.DataFrame(data)
print(df)