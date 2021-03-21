# Python program to find smallest number in a list

list = [1,23,25,10]
print("print the list before operation:")
print(list)
list.sort()
print("print the smallest number in a list:", *list[:1])


# Method 2 using min() method write a program to find smallest number in a list

list1 = [25,56,20,10,3]
print("\n print the list before operation:")
print(list1)
print("\n print the smallest number in a list:", min(list1))


# Method 3  Using the find min list element on inputs provided by user

list2 = []
num = int(input("enter number of elements in list:"))
for i in range(1, num+1):
    ele = int(input("enter ur number:"))
    list2.append(ele)
print("\n print the smallest number in a list:", min(list2))
