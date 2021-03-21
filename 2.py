# Given a list in Python and provided the positions of the elements,
# write a program to swap the two elements in the list.

def swapList(List, pos1, pos2):
    List[pos1], List[pos2] = List[pos2], List[pos1]
    return List
List = [20,15,25,30,35]
pos1,pos2 = 1,2
print(swapList(List,pos1-1,pos2-1))
