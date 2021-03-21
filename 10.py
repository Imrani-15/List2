# Python program to print even numbers in a list

print("\nprint even numbers in a list:")
list = [10,52,62,42,85,23]
for num in list:
    if num % 2 == 0:
        print(num, end = " ")
print("\n")

# Using while loop
print("\nUsing while loop:")
list1 = [20,52,36,45,22]
n = 0
while (n < len(list1)):
    if n % 2 == 0:
        print(list1[n],end=" ")
    n = n + 1
print("\n")

# Using list comprehension

list2 = [10, 21, 4, 45, 66, 93]
even_no = [num for num in list2 if num % 2 == 0]
print("\n even numbers of list:", even_no)

# Using lambda function
list3 = [10, 21, 4, 45, 66, 93, 11]
even = list(filter(lambda x: (x%2 == 0),list3))
print(even)


