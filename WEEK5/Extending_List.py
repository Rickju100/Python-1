"""Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
n should be an input to the user
Use a For loop
Example Expected Output:
Sample list : ['p', 'q']
n = 5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']"""

lista_dada = ["a","b","c","d"]
n = int(input("Select the value of n: "))

lista_no_dada = []

for i in range(1, n+1):
    for value in lista_dada:
        lista_no_dada.append(value+str(i))

print(lista_no_dada)