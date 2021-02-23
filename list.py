list = []
n = int(input("enter the number of elements:"))

for x in range(0, n):
    element = input("enter element:")
    list.append(element)

print("your current list is:", list)

temp = list[0]
list[0] = list[n - 1]
list[n - 1] = temp

print("new list is:", list)

