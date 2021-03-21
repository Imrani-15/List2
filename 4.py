# Using clear() function

list = ['apple','cat','ball','grapes']
print("\n print the list before clear the list:", list)
list.clear()
print("\n printing the list after clear the list:", list)

# using clear() function method 2

list1 = [10,20,30,40,50]
print("\n list before  deleting is:", list1)
list2 = list1 * 0
print("\n list after deleting is:", list2)
#print(list2)

# Using clear() function method 3

l1 = ['suma','mira','hema','ram']
l2 = [10,15,20,25,30,35]
print("\n list before deleting is:", l1)
del l1[:]
print("\n list after deleting is:", l1)
print("\n list2 before deleting is:", l2)
del l2[:]
print("\n list2 after deleting is:",l2)
