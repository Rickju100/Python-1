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
    try: 
        data_dict = openSheet.get_all_records()
        return data_dict
    except:
        return None

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
    x = input

    cell = openSheet.find(x)
    openSheet.update_cell(cell.row,cell.col+1,upd)

def addCarrito():
    lista = []


    while True: 
        productos = input("Enter the product name or End Finish: ").capitalize()
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
    return SUM

#This funcion will allows to  find all the cells matching  a value and update a colum
#a = input("enter a value: ").capitalize()
def findAll(value): #I need to be really carefull with the value parameter, the spaces need to match on cell list or will not get a value match
    cell_list = openSheet.findall(value)
    print(f"({cell_list} here")
    print(cell_list[0].col)
    data1 = cell_list[0].row 
    data2 = cell_list[1].row
    if data1 > data2:
        print(data2)
        lista_Acomodada = [cell_list[1],cell_list[0]]
        print(lista_Acomodada)
        print(lista_Acomodada[0].row,lista_Acomodada[0].col)
        
        rowcol1 = rowcol_to_a1(lista_Acomodada[0].row,lista_Acomodada[0].col+1)
        #Here i need to get the value from rowcol, and then i will print it in the other colum
        gett = openSheet.get(rowcol1)

        price = gett[0][0]
        print(price)
        #Here i just need to update the other colum with the prices
        rowcol2 = rowcol_to_a1(lista_Acomodada[1].row,lista_Acomodada[1].col+1)
        openSheet.update_acell(rowcol2,price)
    
    elif data1 < data2 or data1 == data2: #ask how to solve the problem when the value has an empty space example "Salt " vs "Salt"
        
        rowcol1 = rowcol_to_a1(cell_list[0].row,cell_list[0].col+1)
        #Here i need to get the value from rowcol, and then i will print it in the other colum
        gett = openSheet.get(rowcol1)

        price = gett[0][0]
        print(price)
        #Here i just need to update the other colum with the prices
        rowcol2 = rowcol_to_a1(cell_list[1].row,cell_list[1].col+1)
        openSheet.update_acell(rowcol2,price)
    else: 
        print("Error!")
#IMPORTAN
#Here i used List Comprenhension, because get data gives me a list with a dicitonary insidde https://www.youtube.com/watch?v=l8mWvDUwOt4 https://www.udemy.com/tutorial/hands-on-natural-language-processing-using-python/list-comprehension/?utm_source=adwords&utm_medium=udemyads&utm_campaign=Search_DSA_GammaCatchall_NonP_la.EN_cc.ROW-English&campaigntype=Search&portfolio=ROW-English&language=EN&product=Course&test=&audience=DSA&topic=&priority=Gamma&utm_content=deal4584&utm_term=_._ag_169801645584_._ad_700876640599_._kw__._de_c_._dm__._pl__._ti_dsa-1456167871416_._li_9070299_._pd__._&matchtype=&gad_source=2&gclid=Cj0KCQjwo8S3BhDeARIsAFRmkOMBPc7TUY605aWf4RLdwDUsIeOjz65G0YZaG1POFr-WmGl2U3unbBEaAp0REALw_wcB
"""producs = [d["PRODUCTS STORE"] for d in get_data()]
print(producs)"""

findAll("Queso")