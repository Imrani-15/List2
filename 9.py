# Python program to find largest number in a list
list = [20,90,10,23]
print("\n print the list before operation:")
print(list)
list.sort()
print("\n largest number in a list:", list[-1])

# Using max() method
# Method 2
list1 = [12,20,35,45]
print("\n print the list before operation:")
print(list)
print("\n largest number in a list:", max(list1))

# Using input provided by user

list2 = []
num = int(input("\n enter the number of elements in a list:"))
for i in range(1, num+1):
    ele = int(input("enter ur number:"))
    list2.append(ele)
print("\n largest number in a list:", max(list2))