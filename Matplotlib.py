import pandas as pd 
import matplotlib.pyplot as plt 

excel_file = 'Marvellous.xlsx'
data = pd.read_excel(excel_file)

print("All data from excel file :\n ",data)

print("First 5 rows of file :\n",data.head())

print("First 4 rows of file :\n",data.head(4))

print("last 5 rows of file :\n",data.tail())

print("last 3 rows of file :\n",data.tail(3))

print(data.shape)

Sorted_data = data.sort_values(['Name'],ascending =False)
print("Sorted data :\n",Sorted_data)

data['Age'].plot(kind="hist")
plt.show()

data['Age'].plot(kind="barh")
plt.show()