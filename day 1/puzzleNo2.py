import re

numbers = []

F = open("puzzleNo1.txt","r")

for line in F.readlines():
    number = re.match('\d+', line).group(0)
    numbers.append(number)

sum = 2020
numbers_duplicate = numbers.copy()

for firstNumber in numbers:
    numbers_duplicate.pop(0)
    for secondNumber in numbers_duplicate:
        thirdNumber = str(sum - int(firstNumber) - int(secondNumber))
        if numbers.count(thirdNumber) > 0:
            product = int(firstNumber) * int(secondNumber) * int(thirdNumber)
            print(product)
            print(firstNumber)
            print(secondNumber)
            print(thirdNumber)
            break