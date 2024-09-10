
shop_cart = []
price_comparison = []
prices = {
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
    "maiz":"",
}

def buy():
    n = (int(input("How many items would you like to buy? ")))

    for item in range(n): #here im creating the loop for the shoplist, and the client will decide how long the list will be
        if n > 0:
            item_list = input("Enter the product: ")
        shop_cart.append(item_list) #if i want to use Google sheets, here i just call the function from writeGS
        print(shop_cart)


def delete():
    know = input("Do you know the items in the list? Y/N: ")
    if know == "Y":
        dele = input("Which item would you like to delete?: ")
        shop_cart.remove(dele) #if i want to use Google sheets, here i just call the function from writeGS to remove a value
    else:
        print(shop_cart)
        dele = input("Which item would you like to delete?: ")
        shop_cart.remove(dele)

#This function will iterate over the list of shop_cart, will compare every value with the dictionary key and will apenend in the price_comparison to print the amount
def prices():
    for i in shop_cart:
        if i in prices:
            print("a")

def cartFinish():
    for i in shop_cart:
        print(i)
            



