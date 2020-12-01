import re

numbers = []

F = open("puzzleNo1.txt","r")

for line in F.readlines():
    number = re.match('\d+', line).group(0)
    numbers.append(number)

numbers2 = numbers

for i in range(len(numbers2)):
    firstNumber = numbers2.pop(0)

    for j in numbers:
        sum = int(firstNumber) + int(j)
        if sum == 2020:
            product = int(firstNumber) * int(j)
            print(product)
            print(firstNumber)
            print(j)
            break
