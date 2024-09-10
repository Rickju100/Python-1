import gspread 
import pandas as pd

#Accesing the creds
acces = gspread.oauth()

#access the document using the ID
opendoc = acces.open_by_key("1nv6NsjrdKNmBROi1IfDJMgajhfsg4cLbTSyRljH8niQ")

#Acess the specific sheet in the file by id, 0 is the first sheet in the file. gid=0
openSheet = opendoc.get_worksheet_by_id(0)

#Access Data
data = openSheet.get_all_records()#THis get a dictionary
data1 = openSheet.get_all_values()#this get a list

#Pass the data variable into a dataframe
df = pd.DataFrame(data1) #Remember here to place the parameter, or the function will print empy columns and index
print(df)