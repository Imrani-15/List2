# Python | Ways to find length of list
# Method : 1
List = [1,10,2,20,3,30,4,40,50]
print("\n The list is ", List)
count = 0
for i in List:
    count += 1
print("\n The length of the list is:",count)

# Method : 2 Using the len function

list = []
for i in range(15):
    list.append(i)
print(list)
print("\n The length of the list is:", len(list))
