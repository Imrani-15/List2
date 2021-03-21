# Python program to find sum of elements in list
# Method 1
total = 0
list = [10,20,30,40,50,60]
for i in range(0,len(list)):
    total = total + list[i]
print("The sum of elements in list:", total)

# Method 2 Using the While loop

total = 0
i = 0
list1 = [15,45,62,32]
while (i < len(list1)):
    total = total + list[i]
    i = i+1
print("The sum of the elements in list1:", total)

# Method 3 using the sum() method
list2 = [30,52,65,25]
sum_list = sum(list2)
print("The sum of the elements in list2:", sum_list)

