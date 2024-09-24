import shopping_cart as SC 
import gspreading as gpr
import pandas as pd

"""This is the main code, i will use this file to make the request to the other py files.
Mostly i will try here to call the functions, and create the main loop for that"""

print()
print("Welcome to the Shop Cart!")
print("Here is the menu!")


while True:
    print("\n 1.Review the Store Inventory 2.Add an item into the ShopCart 3.Delete an item 4.Review the list 5.Get the total to pay 6.Leave")
    decision = input("Enter the option selected: ")
    print(f"Your selected option was {decision}")
    print("Y for Yes, N for No")
    y_n = input("Y/N?: " ).capitalize()

    if y_n == "Y":
        print("hello")
        if decision == "1":
            gpr.get_data()
            Products = [product["PRODUCTS STORE"] for product in gpr.get_data()] #Important to use gpr.get_data() with the ()
            pRice = [price["PRICES"] for price in gpr.get_data()] #Important to use gpr.get_data() with the ()
            table = pd.DataFrame(pRice,Products)
            print(table)
        elif decision == "2":
            gpr.addCarrito()
        elif decision == "3":
            gpr.clear()
        elif decision == "4":
            pro= gpr.getCol(5)
            pro2 = pro[1:]
            for i in pro2:
                gpr.findAll(i)
            
            TCart = gpr.suma()
            print(f"the total price of your cart is {TCart}")

            pay = int(input("Enter how much would you like to pay: "))

            payment = TCart - pay
            if payment == 0:
                print(f"Thanks for paying the total of your Cart, the total now is {payment}")    
            elif payment < 0:
                print(f"You have overpaid, your credit is: {payment}")  
            if payment > 0:
                print(f"You are still missing to pay {payment}!")  

        elif decision == "5":
            gpr.suma() #I can try to ask how much would like to pay and give the vuelto

    else:
        print("You Selected No!")
