from typing import List

def read_integers() -> List[int]:
    val = str(input()).split(",")
    newList = []
    for i in range(len(val)):
        newList.append(int(val[i]))
    return newList

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
