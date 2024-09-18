#this is created with chatgpt
def addCarrito():
    # Authenticate and open the sheet
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/credentials.json", scope)
    client = gspread.authorize(creds)
    openSheet = client.open("YourSheetName").sheet1  # Modify as needed to select the correct sheet

    # Collect product names
    lista = []
    while True:
        productos = input("Enter the product name (or 'End' to finish): ").capitalize()
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

#This is mine
def addCarrito():
    lista = []


    while True: 
        productos = input("Enter the product name: ").capitalize()
        if productos == "End":
            break
        else:
            lista.append(productos)
    
    #Check this, for update a full collum with the value of the list
    #cellList = openSheet.range("E2:E")
    """for i in lista: 
        openSheet.update_cells("E2:E20",i)"""
    cellList = openSheet.range('E2:E20')
    cell = openSheet.find("PRODUCTS CART")


    for cell in cellList:
        openSheet.update_cell(cell.row+1,cell.col,lista)

