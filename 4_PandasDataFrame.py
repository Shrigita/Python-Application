import pandas as pd 

df = pd.DataFrame({'Data':[11,21,51,101,111,121],'Label':[101,201,301,401,501,601]})

writer =pd.ExcelWriter('MarvellousPandas.xlsx',engine ='xlsxwriter')

df.to_excel(writer,sheet_name ='sheet1')

writer.save()