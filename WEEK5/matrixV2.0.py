
Lista1 = []
Lista2 = []
Lista3 = []

Lista_General= [Lista1, Lista2, Lista3]


print("Please enter 9 numbers!")

for i in range(9):
    a = int(input("Enter a number:"))
    if i < 3:
        Lista1.append(a)
    elif i< 6:
        Lista2.append(a)
    else:
        Lista3.append(a)
      

print(Lista_General[0])
print(Lista_General[1])
print(Lista_General[2])