# reversing a list
# Method 1 Using the reversed() buitl in function

def Reverse(lst):
    return [ele for ele in reversed(lst)]
lst = [10,12,13,15,14,16]
print("\n This is frist method of reversing a list:")
print(Reverse(lst))

# Method 2 Using the reverse() built in function

def reverse(list):
    list.reverse()
    return list
list = [1,2,3,4,5,6,7]
print("\n This is second method of reversing a list:")
print(reverse(list))

# Method 3 using the slicing

def slicing(list1):
    newlist = list1[::-1]
    return list1
list1 = [15,16,46,47,52,12]
print("\n This is third method of reversing a list:")
print(slicing(list1))

