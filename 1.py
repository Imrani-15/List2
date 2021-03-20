# Given a list, write a Python program to swap first and last element of the list.
def swap(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
newList = [25,12,20,15]
print(swap(newList))

# second way to do the python program to swap first and last element ot the list

def swaplist(List):
    first = List.pop(0)
    last = List.pop(-1)
    List.insert(0,last)
    List.append(first)
    return List
List = [10,20,30,50,95]
print(swaplist(List))