import gspread 
import pandas as pd
from gspread.utils import rowcol_to_a1

#Accesing the creds
acces = gspread.oauth()

#access the document using the ID
opendoc = acces.open_by_key("1nv6NsjrdKNmBROi1IfDJMgajhfsg4cLbTSyRljH8niQ")

#Acess the specific sheet in the file by id, 0 is the first sheet in the file. gid=0
openSheet = opendoc.get_worksheet_by_id(0)

def get_data():#THis get a dictionary
    data_dict = openSheet.get_all_records()
    return data_dict

#Pass the data variable into a dataframe
"""df = pd.DataFrame(data) #Remember here to place the parameter, or the function will print empy columns and index
print(df)
"""

#Access an specific row
def getrow(row):
    values_list = openSheet.row_values(row)
    return values_list


#Access an specific colum
def getCol(col):
    values_list = openSheet.col_values(col)
    return values_list #Here i need to be really carefull, since i need getcol to storage the values, i need a return, i cant do a print, otherwise the next funcion for match will keep giving  TypeError: argument of type 'NoneType' is not iterable'


#Find a product in the sheet
def search(item):
    cell = openSheet.find(item)
    return cell

#This function wiill edit the value next to the key
def edit(x,upd): 
    cell = openSheet.find(x)
    openSheet.update_cell(cell.row,cell.col+1,upd)

#This function will clear the specific value that i provide as argument
def clear(x):
    cell = openSheet.find(x)
    cell_range = rowcol_to_a1(cell.row,cell.col)
    openSheet.batch_clear([cell_range])
    
def valuesAsInt():
    values = getCol(2)
    v = int(''.join(map(str, values)))
    return v

def suma(): #I was gonna cryyy, it was not working due to first value in col is prices, so i was not able to int(i) due to that string
    prices = []
    values = getCol(2)
    
    for i in values[1:]: #Remeber here, to get value starting from index 1, so the list skip prices which is index 0
        prices.append(int(i))
    print(prices)
    SUM = sum(prices)
    print(SUM)
    

"""
#this function will the the argument for the match inside the colum
def match(a):
    match =  openSheet.find(a)
    ubicacion = (match.row, match.col)
    lista = ubicacion
    val = lista[0]
    print(val)
    values = openSheet.acell("B{val}").value
    print(values)
"""

"""
def match(a):
    val = getCol(1)
    if a in val:
        look = search(a)


a = input("Enter the product: ").capitalize()  
#x= input("Enter the price: ").capitalize()     """ 

suma()

