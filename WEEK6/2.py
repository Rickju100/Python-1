numbers = [1, 2, 4, 6, 8, 10, 12, 13]
target = int(input("Target number: "))

seen_numbers = set()
numList = []

for number in numbers:
    complement = target - number
    if complement in seen_numbers:
        numList.append([complement, number])
    seen_numbers.add(number)

print(numList)