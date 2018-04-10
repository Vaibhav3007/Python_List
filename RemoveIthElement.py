a = []
n = int(input("Enter the number of elements in list: "))
for x in range(0,n):
    elements = input("Enter element" + str(x+1) + ":")
    a.append(elements)

element = input("Enter element to operate- ")

count = 0
for i in range(len(a)):
    if a[i] == element:
        count += 1
        
print("The element",element,"occurs",count,"times")
print(a)

num = int(input("Enter which element to remove- "))


c = 0
for x in range(len(a)):
    if a[x] == element:
        c += 1
        if c == num:
            del a[x]
            break
            
        
print(a)
