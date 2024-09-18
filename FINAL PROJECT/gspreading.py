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
    return cell.row,cell.col

def searchNextItem(item):
    cell = openSheet.find(item)
    return cell.row,cell.col+1

#This function wiill edit the value next to the key
#x is the value/item that i want to look for, update is the value i want to store
def edit(x,upd): 
    cell = openSheet.find(x)
    openSheet.update_cell(cell.row,cell.col+1,upd)

def addCarrito():
    lista = []


    while True: 
        productos = input("Enter the product name: ").capitalize()
        if productos == "End":
            break
        else:
            lista.append(productos)
    
    # Update the cells in the Google Sheet
    cell_list = openSheet.range('E2:E' + str(len(lista) + 1))  # Define the range dynamically based on the list length
    
    # Make sure the length of cell_list and lista match
    if len(cell_list) != len(lista):
        raise ValueError("Mismatch between the number of cells and the number of products")

    # Update the cells with product names
    for cell, product in zip(cell_list, lista):
        cell.value = product
    
    # Update the sheet with new values
    openSheet.update_cells(cell_list, value_input_option="USER_ENTERED")



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
  
    values = getCol(6)
    
    for i in values[1:]: #Remeber here, to get value starting from index 1, so the list skip prices which is index 0
    
        prices.append(float(i)) #Here i need to be very carefull, due to sums as floats, needs to make a conditional for what happens if the value is already a float
    print(prices)
    print("here")
    SUM = sum(prices)
    print(SUM)

#This funcion will allows to  find all the cells matching  a value and update a colum
a = input("enter a value: ").capitalize()
def findAll(value):
    cell_list = openSheet.findall(value)
    lista_Acomodada = [cell_list[1],cell_list[0]]
    print(lista_Acomodada)
    print(lista_Acomodada[0].row,lista_Acomodada[0].col)
    
    rowcol = rowcol_to_a1(lista_Acomodada[0].row,lista_Acomodada[0].col+1)
    #Here i need to get the value from rowcol, and then i will print it in the other colum
    gett = openSheet.get(rowcol)
    price = gett[0][0]
    print(price)
    #Here i just need to update the other colum with the prices
    


findAll(a)