#calculate sales tax (IVA) 13%
#Calculate 10%

item = int(input("Which is the item price: "))
amount = int(input("Whow many items do you want: "))

sales = item * amount
iva = sales * 0.13 #tax calculation
discount = sales *0.10 #discount
final = sales - discount


print(discount)
print(f'The price of the product per unit is {item}, the full price of the items is {sales}, the sales tax is {iva}, the total discount is {discount} and the final price is {final}')