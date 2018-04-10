a1 = []
n = int(input("Enter number of elements: "))
for y in range(n):
    element = int(input("Enter element"+str(y+1)+": "))
    a1.append(element)
    
print("The inputed list",a1)

#a = [12,13,54,34,90,36,51,78,25,50]
l = int(input("Enter starting- "))
u = int(input("Enter ending- "))

print("Items in range from list- ")
for x in a1:
    if x >= l and x <= u:
        print(x,end = " ")
