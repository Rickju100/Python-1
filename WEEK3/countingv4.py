
try: 
    number = int(input("Enter a number higher than 0: "))
    count = 1
     
    while count <= number:
        print(count)
    count += 1
    
except NameError:
    print("error")