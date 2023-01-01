import pandas as pd

execel_file ='Marvellous(1).xlsx'
batches =pd.read_excel(execel_file)

print(batches.head(7))
print(batches.tail())

batches_sheet1 =pd.read_excel(execel_file,sheet_name = 0,index_col = 0)
print(batches_sheet1.head())