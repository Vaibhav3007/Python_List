a = []
n = int(input("Enter the number of elements in list: "))
for x in range(0,n):
    elements = input("Enter element" + str(x+1) + ":")
    a.append(elements)

maxx = 0
for i in range(n):
    if len(a[i]) > maxx:
        maxx = len(a[i])
        j = i

print("Longest word in the list",a,"is",a[j])
