def add_two_numbers() -> int:
    userInput = str(input())
    newList = userInput.split(',')
    total = 0
    for i in range(len(newList)):
        total += int(newList[i])
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
